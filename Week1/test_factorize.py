import unittest
from factorize import factorize


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """ Что типы float и str (значения 'string', 1.5) вызывают исключение TypeError """
        with self.subTest(x='string'):
            self.assertRaises(TypeError, factorize, 'string')

        with self.subTest(x=1.5):
            self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        """ Что для отрицательных чисел -1, -10 и -100 вызывается исключение ValueError. """
        cases = [-1, -10, -100]
        for x in cases:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        """ Что для числа 0 возвращается кортеж (0,), а для числа 1 кортеж (1,) """
        cases = [0, 1]
        for x in cases:
            with self.subTest(x=x):
                result = factorize(x)
                test_result = []
                test_result.append(x)
                self.assertEqual(result, tuple(test_result))

    def test_simple_numbers(self):
        """ Что для простых чисел 3, 13, 29 возвращается кортеж, содержащий одно данное число. """
        cases = [3, 13, 29]
        for x in cases:
            with self.subTest(x=x):
                result = factorize(x)
                test_result = []
                test_result.append(x)
                self.assertEqual(result, tuple(test_result))

    def test_two_simple_multipliers(self):
        """ Что для чисел 6, 26, 121 возвращаются соответственно кортежи (2, 3), (2, 13) и (11, 11). """
        cases = {
            6: (2, 3),
            26: (2, 13),
            121: (11, 11)
        }

        for x in cases:
            with self.subTest(x=x):
                result = factorize(x)
                self.assertEqual(result, cases[x])

    def test_many_multipliers(self):
        """ Что для чисел 1001 и 9699690 возвращаются соответственно кортежи (7, 11, 13) и (2, 3, 5, 7, 11, 13, 17,
        19). """
        cases = {
            1001: (7, 11, 13),
            9699690: (2, 3, 5, 7, 11, 13, 17, 19)
        }

        for x in cases:
            with self.subTest(x=x):
                result = factorize(x)
                self.assertEqual(result, cases[x])
