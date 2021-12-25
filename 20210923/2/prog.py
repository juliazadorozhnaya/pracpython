res = 0
n = int(input())
while 1:
    if n <= 0:
        print(n)
        break
    else:
        res += n
        if res > 21:
            print(res)
            break
    n = int(input())
