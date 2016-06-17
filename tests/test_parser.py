import math
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

    def test_parse_operand_real(self):
        self.assertEqual(calculator.parse_operand("1.2"), 1.2)
        self.assertEqual(calculator.parse_operand("pi"), math.pi)

if __name__ == "__main__":
    unittest.main()
