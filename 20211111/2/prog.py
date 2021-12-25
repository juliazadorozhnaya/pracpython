class InvalidInputException(ValueError):
    pass


class BadTriangleException(ValueError):
    pass


def TriangleSquare(inp):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inp)
    except:
        raise InvalidInputException
    if x1 == x2 and x2 == x3:
        raise BadTriangleException
    try:
        a = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
        b = (((x3 - x2) ** 2) + ((y3 - y2) ** 2)) ** (1 / 2)
        c = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** (1 / 2)
    except:
        raise BadTriangleException

    if not ((a < b + c) and (c < b + a) and (b < a + c)):
        raise BadTriangleException
    p = (a + b + c) / 2
    square = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

    if not square:
        raise BadTriangleException
    return square


while True:
    try:
        s = TriangleSquare(input())

    except (InvalidInputException, KeyboardInterrupt):
        print('Invalid input')
    except BadTriangleException:
        print('Not a triangle')
    else:
        print(f"{s:.2f}")
        break

"""
(31245145, 32552345), (67547, 234123), (67547, 234123)
NO
("oh", "step"), ("triangle", "I"), ("am", "stuck")
(0, 0), (4, 0), (4, 1)


"""
