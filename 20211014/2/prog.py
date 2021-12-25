def scale(A, B, a, b, x):
    return (x - A) / (B - A) * (b - a) + a

W, H, A, B, F = input().split()
W = int(W)
H = int(H)
A = float(A)
B = float(B)

X = [scale(0, W-1, A, B, i) for i in range(W)]
Y = [eval(F) for x in X]
my, My = min(Y), max(Y)

res = [' ' * len(X) for j in range(len(Y))]

for i, x in enumerate(X):
	point = eval(F)
	j = 0
	while Y[j] < point:
		j += 1
	res[j] = res[j][:i] + '*' + res[j][i+1:]

for el in res[::-1]:
	print(el)

