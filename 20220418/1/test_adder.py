import unittest
import adder
import random

class TestAdder(unittest.TestCase):
    
    def setuUp(self):
        self.A, self.B = random.randrange(0 ,100), random.randrange(0 , 100)
        self.C = self.A + self.B
        self.S, self.T = "QWE", "rty" 
    
    def test_numbers(self):
        self.unittest.asserEqual(adder.adder(self.A, self.B), self.C)
        
    def test_strings(self):
        self.assertEqual(adder.adder(self.S, self.T), "QWErty")
        
    def test_exception(self):
        with self.assertRaises(TypeError):
            adder.adder(123)