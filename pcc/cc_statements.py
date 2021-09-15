import contextlib
from dataclasses import dataclass
from io import IOBase
from typing import Sequence, Optional, Tuple


@dataclass
class ComputercraftStatements(object):
    stream: IOBase

    @contextlib.contextmanager
    def While(self, condition: str):
        self.stream.write(f'while({condition})\ndo\n')
        yield
        self.stream.write('end\n')

    @contextlib.contextmanager
    def For(self, var_name: str, init: int, min_max: int, increment: int):
        self.stream.write(f'for {var_name}={init}, {min_max}, {increment}\ndo\n')
        yield var_name, lambda write: self.stream.write('break\n', write)
        self.stream.write('end\n')

    # condition = [condition, action]
    def If(self, conditions: Sequence[Tuple[str, str]], else_action: Optional[str] = None):
        first = True
        for condition in conditions:
            self.stream.write(f'{"if" if first else "elseif"} {condition[0]} then\n{condition[1]}\n')
            first = False
        if else_action:
            self.stream.write(f'else\n{else_action}\n')
        self.stream.write('end\n')

    def Equals(self, a: str, b: str):
        return a + ' == ' + b

    def Greater(self, a: str, b: str, and_equals: bool = False):
        return a + f' >{"=" if and_equals else ""}' + b

    def Lesser(self, a: str, b: str, and_equals: bool = False):
        return a + f' <{"=" if and_equals else ""}' + b

    def And(self, a: str, b: str):
        return a + ' and ' + b

    def Or(self, a: str, b: str):
        return a + ' or ' + b

    def Not(self, a: str):
        return 'not ' + a

    @contextlib.contextmanager
    def Function(self, func_name, *parameters, write=True):
        def call_self(*params, write=True):
            return self.stream.write(func_name + '(' + ','.join(params) + ')', write=write)
        self.stream.write(f'function {func_name} ({",".join(parameters)})\ndo\n', write=write)
        yield call_self, parameters
        self.stream.write('end\n', write=write)

    def Variable(self, name, value, write=True):
        self.stream.write(name + '=' + value.__repr__() + '\n', write=write)
        return name
