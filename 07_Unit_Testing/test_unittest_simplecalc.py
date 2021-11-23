#Test for the code to pass

from simple_calc import SimpleCalc # we will make a simple calculator
import unittest

class SimpleCalcTests(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalc()

    #def tearDown(self): # Opposite to set up, removes unwanted test products

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)
    def test_subtract(self):
        actual = self.calc.subtract(4, 2)
        expected = 2
        self.assertEqual(actual, expected)
    def test_multiply(self):
        actual = self.calc.multiply(5, 2)
        expected = 10
        self.assertEqual(actual, expected)
    def test_divide(self):
        actual = self.calc.divide(20, 2)
        expected = 10
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest = SimpleCalcTests()