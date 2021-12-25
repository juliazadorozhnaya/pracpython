from types import FunctionType


def dec(func):
    def new_func(self, *args, **kwargs):
        print('{}: {}, {}'.format(func.__name__, args, kwargs))
        return func(self, *args, **kwargs)
    return new_func


class dump(type):
    def __new__(cls, name, bases, dct):
        new_funcs = {}
        for name, func in dct.items():
            if isinstance(func, FunctionType):
                func = dec(func)
            new_funcs[name] = func
        dct = new_funcs
        return super().__new__(cls, name, bases, dct)

import sys
exec(sys.stdin.read())