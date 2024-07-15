cmake_minimum_required(VERSION 3.25)
project(wheelbind)

set(CMAKE_CXX_STANDARD 17)
# module的名称一定要和setup.py对应起来，不然很多自动化操作没法执行
set(PY_MODULE_NAME "mylibrary_C")
if (NOT PY_MODULE_NAME)
    set(PY_MODULE_NAME "mylibrary_C")
endif ()
option(BUILD_PYTHON "build python package" ON)


file(GLOB HEAD ${PROJECT_SOURCE_DIR}/src/*.h)
file(GLOB SRC ${PROJECT_SOURCE_DIR}/src/*.cpp ${PROJECT_SOURCE_DIR}/src/*.cc)
list(REMOVE_ITEM SRC ${PROJECT_SOURCE_DIR}/src/export_py.cpp)

add_library(wheelbind SHARED ${HEAD} ${SRC})
include(GenerateExportHeader)
generate_export_header(wheelbind EXPORT_FILE_NAME ${PROJECT_SOURCE_DIR}/src/exports.h)

add_executable(wheel_Test src/main.cpp)
target_link_libraries(wheel_Test wheelbind)

if (BUILD_PYTHON)
    add_subdirectory(${PROJECT_SOURCE_DIR}/third_part/pybind11)
    configure_file(${PROJECT_SOURCE_DIR}/src/config.h.in ${PROJECT_SOURCE_DIR}/src/config.h)
    pybind11_add_module(${PY_MODULE_NAME} MODULE ${SRC} ${PROJECT_SOURCE_DIR}/src/export_py.cpp)
endif ()


