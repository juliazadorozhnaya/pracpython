n = int(input())
i = n
while i < n+3:
    j = n
    while j < n+3:
        num = i * j
        if num == 6 or (num > 10 and num // 10 + num % 10 == 6):
            print(i, "*", j, "=:=)", sep="", end=" ")
        else:
            print(i, "*", j, "=", i * j, sep="", end=" ")
        j += 1
    i += 1
    print("")


