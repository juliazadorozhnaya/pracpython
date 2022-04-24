import unittest
import prog
from unittest.mock import MagicMock

eps = pow(10, -5)

def make_test(coefficient, true_answer):
    prog.SquareIO.inputCoeff = MagicMock(side_effect=coefficient)
    prog.SquareIO.printResult = MagicMock()
    prog.solveSquare()
    result = prog.SquareIO.printResult.call_args.args[0]

    
    if type(result) != type(true_answer):
        assert False
    elif result is None or type(result) is str:
        assert result == true_answer
    elif type(result) is float: 
        if len(result) == len(true_answer):
            if len(result) == 2 == len(true_answer) and type(result) is tuple: 
                assert abs(result[0] - true_answer[0]) < eps and abs(result[1] - true_answer[1]) < eps
            elif len(result) == 1: 
                assert abs(result[0] - true_answer[0]) < eps
            else:  
                assert False
        else:
            assert False
                          
class TestSolver(unittest.TestCase):
    
    def test_above_zero(self):
        make_test((1, -3, 2), (1.0, 2.0))

    def test_equal_zero(self):
        make_test((1, -4, 4), (2.0, 2.0))

    def test_less_zero(self):
        make_test((4, 2, 1), 'there is no solution')

    def test_linear(self):
        make_test((0, 5, -7), (1.4,))

    def test_degenerate(self):
        make_test((0, 0, 9), 'there is no solution')

    def test_all_zero(self):
        make_test((0, 0, 0), 'x values - any numbers')

    def test_wrong_input(self):
        make_test((1, "-1-", 0), "wrong number entered")