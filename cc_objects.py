import abc
from dataclasses import dataclass
from io import IOBase


@dataclass
class CCObject(abc.ABC):
    stream: IOBase

    def __getattr__(self, item):
        def function(*args, write=True):
            return self.stream.write(f'{self.__class__.__name__.lower()}.{item}({",".join(args)})\n', write=write)
        function.__name__ = f'{self.__class__.__name__}.{item}'
        return getattr(super(CCObject, self), item, function)


class Bit(CCObject):
    pass


class Colors(CCObject):
    pass


class Commands(CCObject):
    pass


class Coroutine(CCObject):
    pass


class Disk(CCObject):
    pass


class Fs(CCObject):
    pass


class Gps(CCObject):
    pass


class Help(CCObject):
    pass


class HTTP(CCObject):
    pass


class IO(CCObject):
    pass


class Keys(CCObject):
    pass


class Math(CCObject):
    pass


class MultiShell(CCObject):
    pass


class OS(CCObject):
    pass


class PaintUtils(CCObject):
    pass


class Parallel(CCObject):
    pass


class Peripheral(CCObject):
    pass


class Rednet(CCObject):
    pass


class Redstone(CCObject):
    pass


class Settings(CCObject):
    pass


class Shell(CCObject):
    pass


class String(CCObject):
    pass


class Table(CCObject):
    pass


class Term(CCObject):
    pass


class TextUtils(CCObject):
    pass


class Turtle(CCObject):
    pass


class Vector(CCObject):
    pass


class Window(CCObject):
    pass
