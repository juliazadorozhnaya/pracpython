def dominate(pa, com):
    if pa[0] <= com[0] and pa[1] <= com[1] and (pa[0] < com[0] or pa[1] < com[1]):
        return True
    return False


def Pareto(*args):
    res = []
    for pa in args:
        ind = 0
        for com in args:
            if dominate(pa, com):
                ind = 1
        if not ind:
            res.append(pa)
    return tuple(res)

print(Pareto(*eval(input())))

import sys
exec(sys.stdin.read())
