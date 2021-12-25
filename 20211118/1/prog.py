def objcount(cls):
    class count(cls):
        cls.counter = 0
        def __init__(self, *args, **kwargs):
            #super().__init__(*args, **kwargs)
            cls.counter += 1

        def __del__(self, *args, **kwargs):
            cls.counter -= 1
    return count

import sys
exec(sys.stdin.read())

