import unittest
import adder

class TestAdder(unittest.TestCase):
    
    def test_numbers(self):
        self.unittest.asserEqual(adder.adder(100500, 42), 100542)
        
    def test_strings(self):
        self.assertEqual(adder.adder("QWE", "rty"), "QWErty")
        
    def test_exception(self):
        adder.adder(123)