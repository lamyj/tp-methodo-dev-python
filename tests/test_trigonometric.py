import unittest

import calculator

class TestTrigonometric(unittest.TestCase):
    def test_cos(self):
        result = calculator.cos("0")
        self.assertEqual(result, "1.0")

    def test_sin(self):
        result = calculator.sin("0")
        self.assertEqual(result, "0.0")

    def test_sin_pi(self):
        result = calculator.sin("pi")
        self.assertTrue(float(result) < 1e8)

    def test_tan(self):
        result = calculator.tan("0")
        self.assertTrue(result, "0.0")
