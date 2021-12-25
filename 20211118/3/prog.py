from string import ascii_lowercase


class Alpha:
    __slots__ = [*ascii_lowercase]

    def __init__(self, *args, **kwargs):
        for char, value in kwargs.items():
            self.__setattr__(char, value)

    def __str__(self):
        result = []
        for char in self.__slots__:
            try:
                result.append(f"{char}: {self.__getattribute__(char)}")
            except AttributeError as e:
                pass
        return ', '.join(result)


class AlphaQ:
    def __init__(self, *args, **kwargs):
        for char, value in kwargs.items():
            self.__setattr__(char, value)

    def __str__(self):
        result = []
        for char in sorted(self.__dict__):
            try:
                result.append(f"{char}: {self.__getattr__(char)}")
            except AttributeError as e:
                pass
        return ', '.join(result)

    def __getattr__(self, item):
        if item in ascii_lowercase:
            return self.__dict__[item]
        raise AttributeError

import sys
exec(sys.stdin.read())
