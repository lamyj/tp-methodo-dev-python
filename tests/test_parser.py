import unittest

import calculator

class TestParser(unittest.TestCase):
    def test_parse_operator(self):
        self.assertEqual(calculator.parse_operator("+"), calculator.addition)
        self.assertEqual(calculator.parse_operator("-"), calculator.subtraction)
        self.assertEqual(calculator.parse_operator("*"), calculator.multiplication)
        self.assertEqual(calculator.parse_operator("/"), calculator.division)

    def test_parse_unknown_operator(self):
        with self.assertRaises(Exception):
            calculator.parse_operator(".")

if __name__ == "__main__":
    unittest.main()
