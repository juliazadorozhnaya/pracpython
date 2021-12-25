import sys
from operator import add
from functools import reduce

N_b = sys.stdin.buffer.read(1)
N = int(N_b[0])
data = sys.stdin.buffer.read()
L = len(data)
Z = N_b + reduce(add, sorted(data[i * L // N:(i + 1) * L // N] for i in range(N)))
sys.stdout.buffer.write(Z)
