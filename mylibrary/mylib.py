from . import mylibrary_C


class MyLibrary:
    def __int__(self):
        self.lib = mylibrary_C.MyLibrary()

    def add(self, x: int, y: int) -> int:
        return x + y

    def sub(self, x: int, y: int) -> int:
        return x - y
