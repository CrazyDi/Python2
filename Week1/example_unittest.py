import unittest
from fibonacci import fibo


class TestFibonacciNumbers(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fibo(0), 0)

    def test_simple(self):
        for n, fib_n in (1, 1), (2, 1), (3, 2), (4, 3), (5, 5):
            with self.subTest(i=n):
                self.assertEqual(fibo(n), fib_n)

    def test_positive(self):
        self.assertEqual(fibo(10), 56)

    def test_negative(self):
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fibo, -1)
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fibo, -10)


if __name__ == "__main__":
    unittest.main()
