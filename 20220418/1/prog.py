def solveSquare(a, b, c):
    D = b ** 2 - 4 * a * c
    
    if D < 0:
        return None
    elif D == 0:
        return (-b/(2 * a), -b/(2 * a))
    else:
        first_root = (-b + D**0.5) / (2 * a)
        second_root = (-b - D**0.5) / (2 * a)
        return (min(first_root, second_root), max(first_root, second_root))

if __name__ == "__main__":
    a, b, c = eval(input())
    solveSquare(a, b, c)