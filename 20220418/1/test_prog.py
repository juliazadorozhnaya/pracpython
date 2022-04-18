
import unittest
import prog


class TestEqu(unittest.TestCase):
    
    def test_greater_zero(self):
        self.assertEqual(prog.solveSquare(1, 3, 2), (-2.0, -1.0))
        
    def test_equal_zero(self):
        self.assertEqual(prog.solveSquare(1, 4, 4), (-2, -2))
        
    def test_lower_zero(self):
        self.assertEqual(prog.solveSquare(5, 2, 3), None)
        

        