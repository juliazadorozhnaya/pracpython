M, N = eval(input())
print([k for k in range(M, N) if (k > 1) and all([(k%i != 0) for i in range(2, k)])])
