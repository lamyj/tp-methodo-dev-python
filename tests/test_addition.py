import unittest

import calculator

class TestAddition(unittest.TestCase):
    def test_two_positive_integers(self):
        result = calculator.addition("12", "34")
        self.assertEqual(result, "46.0")

    def test_one_positive_one_negative_integer(self):
        result = calculator.addition("12", "-34")
        self.assertEqual(result, "-22.0")

    def test_two_reals(self):
        result = calculator.addition("12.34", "45.67")
        self.assertEqual(result, "58.01")

if __name__ == "__main__":
    unittest.main()
