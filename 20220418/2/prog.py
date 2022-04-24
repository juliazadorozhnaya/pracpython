class SquareIO:
    
    def __init__(self):
        pass

    def inputCoeff(self, name):
        coeff_value = input(f"Input {name}:")
        return coeff_value

    def printResult(self, result):
        print(f"Solution: {result}")

def solveSquare():
    try: 
        a = float(SquareIO().inputCoeff('a'))
        b = float(SquareIO().inputCoeff('b'))
        c = float(SquareIO().inputCoeff('c'))
    except Exception:
        SquareIO().printResult('wrong number entered')
    else:
        if a == 0:
            if b == 0:
                if c == 0:
                    SquareIO().printResult('x values - any numbers')
                else:
                    SquareIO().printResult('there is no solution')
            elif b!=0 and c == 0:
                SquareIO().printResult((c / b,))
            else:
                SquareIO().printResult((-c / b,) )
        else:
            D = b * b - 4 * a * c
            if D > 0:
                SquareIO().printResult(((-b - D**0.5) / 2 * a, (-b + D**0.5) / 2 * a))
            
            elif D == 0:
                SquareIO().printResult((-b/(2 * a), -b/(2 * a)))
                
            else:
                SquareIO().printResult('there is no solution')


if __name__ == "__main__":
    solveSquare()