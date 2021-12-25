from math import *

commands = dict()  # f[name] = ((arg1, arg2, ...), expr)

counter = 0

while True:
    counter += 1
    cmd = input()

    if cmd.startswith(':'):
        name, *args, expr = cmd[1:].split()
        commands[name] = (tuple(args), expr)
        continue

    name, *vals = cmd.split()
    if name == 'quit':
        if len(vals) > 0:
            print(eval(vals[0].format(len(commands) + 1, counter)))
        break

    var_names = commands[name][0]
    expr = commands[name][1]

    var_dict = {vr: eval(vl) for vr, vl in zip(var_names, vals)}
    res = eval(expr, globals(), var_dict)
    print(res)