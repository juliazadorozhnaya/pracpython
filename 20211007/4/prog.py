from math import *

def Calc(s, t ,u):
	def S(x):
		return eval(s)
	def T(x):
		return eval(t)
	def U(z):
		x = S(z)
		y = T(z)
		return eval(u)
	return U


F = Calc(*eval(input()))
print(F(eval(input())))

import sys
exec(sys.stdin.read())

