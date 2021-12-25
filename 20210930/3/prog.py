a = eval(input())
size = len(a)
mat1 = [a]

for i in range(1, size):
    mat1.append(eval(input()))

mat2 = []
for i in range(size):
    mat2.append(eval(input()))

mat3 = [[0 for i in range(size)] for i in range(size)]

for i in range(size):
    for j in range(size):
        for k in range(size):
            mat3[i][j] += mat1[i][k] * mat2[k][j]

for i in range(size):
    print(mat3[i])
