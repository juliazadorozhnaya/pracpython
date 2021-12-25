def Bisect(x, b):
	if b[len(b) // 2] == x:
		return True
	if len(b) == 1:
		return False
	if b[len(b) // 2] < x:
		return Bisect(x, b[len(b) // 2:])
	return Bisect(x, b[:len(b) // 2])

a, b = eval(input())
print(Bisect(a, b))

import sys
exec(sys.stdin.read())
