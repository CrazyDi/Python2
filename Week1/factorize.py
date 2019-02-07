def factorize(x):
    """ Factorize positive integer and returns its factors
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """

    if type(x) is not int:
        raise TypeError

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


if __name__ == "__main__":
    r = factorize(1001)
    print(r)
