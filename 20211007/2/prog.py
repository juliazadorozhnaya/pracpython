def sub(f, s):
    if hasattr(f, "__sub__") and hasattr(f, "__sub__"):
        return f - s
    res = []
    for el in f:
        if el not in s:
            res.append(el)
    if type(f) is str:
        return ''.join(res)
    return type(f)(res)


print(sub(*eval(input())))

import sys
exec(sys.stdin.read())
