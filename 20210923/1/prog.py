n = int(input())

if n % 25 == 0 and n % 2 == 0:
    print("A +", end=" ")
else:
    print("A -", end=" ")

if n % 25 == 0 and n % 2 != 0:
    print("B +", end=" ")
else:
    print("B -", end=" ")

if n % 8 == 0:
    print("C +", end=" ")
else:
    print("C -", end=" ")
    
