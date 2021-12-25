def check_annotations(self):
    for attr, value in self.__annotations__.items():
        if not hasattr(self, attr) or not isinstance(getattr(self, attr), value):
            return False
    return True


class check(type):
    def __init__(cls, *args, **kwargs):
        setattr(cls, 'check_annotations', check_annotations)
        super().__init__(*args, **kwargs)


import sys
exec(sys.stdin.read())