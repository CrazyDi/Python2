import unittest


def factorize(x):
    """ Factorize positive integer and returns its factors
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """

    if type(x) is not int:
        raise ValueError

    if x < 0:
        raise ValueError

    result = []

    if x == 0 or x == 1:
        result.append(x)
    else:
        d = 2

        while d * d <= x:
            if x % d == 0:
                result.append(d)
                x //= d
            else:
                d += 1
        if x > 1:
            result.append(x)

    return tuple(result)


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """ Что типы float и str (значения 'string', 1.5) вызывают исключение TypeError """
        pass

    def test_negative(self):
        """ Что для отрицательных чисел -1, -10 и -100 вызывается исключение ValueError. """
        pass

    def test_zero_and_one_cases(self):
        """ Что для числа 0 возвращается кортеж (0,), а для числа 1 кортеж (1,) """
        pass

    def test_simple_numbers(self):
        """ Что для простых чисел 3, 13, 29 возвращается кортеж, содержащий одно данное число. """
        pass

    def test_two_simple_multipliers(self):
        """ Что для чисел 6, 26, 121 возвращаются соответственно кортежи (2, 3), (2, 13) и (11, 11). """
        pass

    def test_many_multipliers(self):
        """ Что для чисел 1001 и 9699690 возвращаются соответственно кортежи (7, 11, 13) и (2, 3, 5, 7, 11, 13, 17,
        19). """
        pass


if __name__ == "__main__":
    r = factorize(1001)
    print(r)
