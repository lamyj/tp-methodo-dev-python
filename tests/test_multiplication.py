import unittest

import calculator

class TestMultiplication(unittest.TestCase):
    def test(self):
        result = calculator.addition("1.2", "3.4")
        self.assertEqual(result, "4.6")

if __name__ == "__main__":
    unittest.main()
