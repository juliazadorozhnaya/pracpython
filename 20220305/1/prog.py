import shlex
import readline

while s:=input('>'):
    num, *params = shlex.split(s)
    if int(num) < 0 or int(num) > len(params):
        break
    else:
        print(params[int(num)])