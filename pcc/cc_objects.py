import abc
from dataclasses import dataclass
from io import IOBase


@dataclass
class CCObject(abc.ABC):
    name: str
    stream: IOBase

    def __getattr__(self, item):
        def function(*args, write=True):
            args = ",".join((str(x) if type(x) is not str else '"' + x + '"' for x in args))
            return self.stream.write(f'{self.name.lower()}.{item}({args})\n', write=write)
        function.__name__ = f'{self.__class__.__name__}.{item}'
        return getattr(super(CCObject, self), item, function)


class Bit(CCObject):
    def __init__(self, stream):
        super(Bit, self).__init__('Bit', stream)
    


class Colors(CCObject):
    def __init__(self, stream):
        super(Colors, self).__init__('Colors', stream)


class Commands(CCObject):
    def __init__(self, stream):
        super(Commands, self).__init__('Commands', stream)


class Coroutine(CCObject):
    def __init__(self, stream):
        super(Coroutine, self).__init__('Coroutine', stream)


class Disk(CCObject):
    def __init__(self, stream):
        super(Disk, self).__init__('Disk', stream)


class Fs(CCObject):
    def __init__(self, stream):
        super(Fs, self).__init__('Fs', stream)


class Gps(CCObject):
    def __init__(self, stream):
        super(Gps, self).__init__('Bit', stream)


class Help(CCObject):
    def __init__(self, stream):
        super(Help, self).__init__('Help', stream)


class HTTP(CCObject):
    def __init__(self, stream):
        super(HTTP, self).__init__('HTTP', stream)


class IO(CCObject):
    def __init__(self, stream):
        super(IO, self).__init__('IO', stream)


class Keys(CCObject):
    def __init__(self, stream):
        super(Keys, self).__init__('Keys', stream)


class Math(CCObject):
    def __init__(self, stream):
        super(Math, self).__init__('Math', stream)


class MultiShell(CCObject):
    def __init__(self, stream):
        super(MultiShell, self).__init__('MultiShell', stream)


class OS(CCObject):
    def __init__(self, stream):
        super(OS, self).__init__('OS', stream)


class PaintUtils(CCObject):
    def __init__(self, stream):
        super(PaintUtils, self).__init__('PaintUtils', stream)


class Parallel(CCObject):
    def __init__(self, stream):
        super(Parallel, self).__init__('Parallel', stream)


class Peripheral(CCObject):
    def __init__(self, stream):
        super(Peripheral, self).__init__('Peripheral', stream)


class Rednet(CCObject):
    def __init__(self, stream):
        super(Rednet, self).__init__('Rednet', stream)


class Redstone(CCObject):
    def __init__(self, stream):
        super(Redstone, self).__init__('Redstone', stream)


class Settings(CCObject):
    def __init__(self, stream):
        super(Settings, self).__init__('Settings', stream)


class Shell(CCObject):
    def __init__(self, stream):
        super(Shell, self).__init__('Shell', stream)


class String(CCObject):
    def __init__(self, stream):
        super(String, self).__init__('String', stream)


class Table(CCObject):
    def __init__(self, stream):
        super(Table, self).__init__('Table', stream)


class Term(CCObject):
    def __init__(self, stream):
        super(Term, self).__init__('Term', stream)


class TextUtils(CCObject):
    def __init__(self, stream):
        super(TextUtils, self).__init__('TextUtils', stream)


class Turtle(CCObject):
    def __init__(self, stream):
        super(Turtle, self).__init__('Turtle', stream)


class Vector(CCObject):
    def __init__(self, stream):
        super(Vector, self).__init__('Vector', stream)


class Window(CCObject):
    def __init__(self, stream):
        super(Window, self).__init__('Window', stream)
