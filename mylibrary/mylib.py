from . import mylibrary_C


class Base:
    def __init__(self, x: int):
        self.base = mylibrary_C.Base(x)

    def get_x(self):
        return self.base.get_x()


class MyLibrary(Base):
    def __init__(self, x: int, y: int):
        super(MyLibrary, self).__init__(x)
        self.lib = mylibrary_C.MyLibrary(x, y)
        self.name = self.lib.name

    def add(self, x: int, y: int) -> int:
        return self.lib.add(x, y)

    def sub(self, x: int, y: int) -> int:
        return self.lib.sub(x, y)

    def get_y(self):
        return self.lib.get_y()
