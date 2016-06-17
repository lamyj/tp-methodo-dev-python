import unittest

import calculator

class TestSubtraction(unittest.TestCase):
    def test_two_positive_integers(self):
        result = calculator.subtraction("12", "34")
        self.assertEqual(result, "-22.0")

    def test_one_positive_one_negative_integer(self):
        result = calculator.subtraction("12", "-34")
        self.assertEqual(result, "46.0")

    def test_two_reals(self):
        result = calculator.subtraction("12.34", "45.67")
        self.assertEqual(result, "-33.33")

    def test_pi(self):
        result = calculator.subtraction("pi", "1.2")
        self.assertEqual(result, "1.94")

if __name__ == "__main__":
    unittest.main()
