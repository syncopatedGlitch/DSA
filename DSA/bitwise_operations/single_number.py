def find_single_number(nums):
    res = 0
    for num in nums:
        res = res ^ num
    return res


def tests():
    nums = [2, 4, 5, 6, 4, 6, 2]
    res = find_single_number(nums)
    print(f"res is {res}")
    assert res == 5


tests()
