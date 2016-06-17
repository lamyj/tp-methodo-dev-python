import unittest

import calculator

class TestDivision(unittest.TestCase):
    def test_non_zero(self):
        result = calculator.division("25.6", "8")
        self.assertEqual(result, "3.2")

    def test_zero(self):
        result = calculator.division("1", "0")
        self.assertEqual(result, "nan")

if __name__ == "__main__":
    unittest.main()
