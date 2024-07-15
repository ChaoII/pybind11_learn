import setuptools.command.build_ext

from contextlib import contextmanager
import os
import shlex
import subprocess
import sys
import platform
import multiprocessing
import shutil

TOP_DIR = os.path.realpath(os.path.dirname(__file__))
SRC_DIR = os.path.join(TOP_DIR, "./")
CMAKE_BUILD_DIR = os.path.join(TOP_DIR, '.setuptools-cmake-build')

WINDOWS = (os.name == 'nt')

CMAKE = shutil.which('cmake3') or shutil.which('cmake')
MAKE = shutil.which('make')


@contextmanager
def cd(path):
    if not os.path.isabs(path):
        raise RuntimeError('Can only cd to absolute path, got: {}'.format(path))
    orig_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(orig_path)


class CmakeBuild(setuptools.Command):
    user_options = [(str('jobs='), str('j'),
                     str('Specifies the number of jobs to use with make'))]

    built = False

    def initialize_options(self):
        self.jobs = None

    def finalize_options(self):
        if sys.version_info[0] >= 3:
            self.set_undefined_options('build', ('parallel', 'jobs'))
        if self.jobs is None and os.getenv("MAX_JOBS") is not None:
            self.jobs = os.getenv("MAX_JOBS")
        self.jobs = multiprocessing.cpu_count() if self.jobs is None else int(
            self.jobs)

    def run(self):
        os.makedirs(CMAKE_BUILD_DIR, exist_ok=True)

        with cd(CMAKE_BUILD_DIR):
            build_type = 'Release'
            # configure
            cmake_args = [CMAKE, '-DCMAKE_BUILD_TYPE=%s' % build_type]
            if WINDOWS:
                cmake_args.extend([
                    '-DPY_VERSION={}'.format('{0}.{1}'.format(*sys.version_info[:2])),
                ])
                if platform.architecture()[0] == '64bit':
                    cmake_args.extend(['-A', 'x64', '-T', 'host=x64'])
                else:
                    cmake_args.extend(['-A', 'Win32', '-T', 'host=x86'])
            if 'CMAKE_ARGS' in os.environ:
                extra_cmake_args = shlex.split(os.environ['CMAKE_ARGS'])
                del os.environ['CMAKE_ARGS']
                cmake_args.extend(extra_cmake_args)
            cmake_args.append(TOP_DIR)
            subprocess.check_call(cmake_args)
            # build
            build_args = [CMAKE, '--build', os.curdir]
            if WINDOWS:
                build_args.extend(['--config', build_type])
                build_args.extend(['--', '/maxcpucount:{}'.format(self.jobs)])
            else:
                build_args.extend(['--', '-j', str(self.jobs)])
            subprocess.check_call(build_args)


class BuildExtension(setuptools.command.build_ext.build_ext):
    def run(self):
        self.run_command('cmake_build')
        return super().run()

    def build_extensions(self):
        build_lib = self.build_lib
        # 如果不创建extension_dst_dir那么在pip install -e . 模式下无法正确拷贝so文件
        extension_dst_dir = os.path.join(build_lib, "mylibrary")
        os.makedirs(extension_dst_dir, exist_ok=True)
        for ext in self.extensions:
            fullname = self.get_ext_fullname(ext.name)
            # mylibrary_C.cpython-39-darwin.so
            filename = os.path.basename(self.get_ext_filename(fullname))
            lib_path = CMAKE_BUILD_DIR
            if WINDOWS:
                debug_lib_dir = os.path.join(lib_path, "Debug")
                release_lib_dir = os.path.join(lib_path, "Release")
                if os.path.exists(debug_lib_dir):
                    lib_path = debug_lib_dir
                elif os.path.exists(release_lib_dir):
                    lib_path = release_lib_dir
            # 编译的extension库在CMAKE_BUILD_DIR目录下，那么库的绝对路径其实是src
            src = os.path.join(lib_path, filename)
            # self.build_lib是系统临时目录，注意一定是mylibrary不然找不到库的
            dst = os.path.join(
                os.path.realpath(self.build_lib), "mylibrary", filename)
            # 把编译好的库目录拷贝到/xxxx/xxx/mylibrary/xxx.so
            # 最后会把/xxxx/xxx 里面的目录前部打包到whl中
            self.copy_file(src, dst)


cmdclass = {
    'cmake_build': CmakeBuild,
    'build_ext': BuildExtension,
}

# BuildExtension中的self.Extensions，可以配置很多
ext_modules = [
    setuptools.Extension(
        name=str('mylibrary.mylibrary_C'), sources=[])
]

setuptools.setup(
    ext_modules=ext_modules,
    cmdclass=cmdclass,
)
