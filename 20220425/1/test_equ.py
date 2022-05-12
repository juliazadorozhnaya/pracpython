import unittest
from solve import solve 

class TestEqu(unittest.TestCase):
    numbers = []

    def test0(self):
        """Standard test."""
        self.numbers = [1, 2]
        solve(*self.numbers)
        self.assertEqual(solve(*self.numbers), -2.0)

    def test1(self):
        """Zero test."""
        self.numbers = [0, 2]
        solve(*self.numbers)
        self.assertEqual(solve(*self.numbers), None)
        
    def test2(self):
        """Big Number Test."""
        self.numbers = [123456789, 987654321]
        solve(*self.numbers)
        self.assertEqual(solve(*self.numbers), -8.0000000729)
        
    def test3(self):
        """Test with negative numbers"""
        self.numbers = [3, -348]
        solve(*self.numbers)
        self.assertEqual(solve(*self.numbers), 116.0)
