def is_power_of_two(n):
    # if n <= 0:
    #     return False
    # else:
        # res = n & (n-1)
        # if res == 0:
        #     return True
        # else:
        #     return False
    return n > 0 and (n & (n - 1)) == 0


def tests():
    n = 32
    res = is_power_of_two(n)
    assert res is True
    m = 12
    res = is_power_of_two(m)
    assert res is False


tests()
