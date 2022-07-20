def combinations(*args):

    result = 1
    for i in args:
        if result != 0:
            result *= i
    return result


combinations(4, 2, 2, 2)
