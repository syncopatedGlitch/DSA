'''

'''

from typing import List


def isZeroArray(nums: List[int], queries: List[List[int]]) -> bool:
    n, m = len(nums), len(queries)
    diff = [0] * (n + 1)
    for i in range(m):
        left, right = queries[i][0], queries[i][1]
        diff[left] += 1
        diff[right + 1] -= 1
    running_supply = 0
    supply = []
    for i in range(n):
        running_supply += diff[i]
        supply.append(running_supply)
    for k in range(n):
        if supply[k] < nums[k]:
            return False
    return True


def tests():
    nums = [1, 0, 1]
    queries = [[0, 2]]
    res = isZeroArray(nums, queries)
    print(f"res is {res}")
    assert res is True
    nums = [8]
    queries = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    res = isZeroArray(nums, queries)
    print(f"res is {res}")
    assert res is False
    nums = [2]
    queries = [[0, 0], [0, 0]]
    res = isZeroArray(nums, queries)
    print(f"res is {res}")
    assert res is True
    nums = [3, 5, 0]
    queries = [
        [2, 2],
        [0, 2],
        [2, 2],
        [0, 0],
        [0, 2],
        [0, 2],
        [0, 0],
        [1, 2],
        [2, 2],
        [2, 2],
        [2, 2],
        [0, 2],
        [2, 2],
        [0, 2],
        [2, 2]
    ]
    res = isZeroArray(nums, queries)
    print(f"res is {res}")
    assert res is True
    nums = [0, 3, 9]
    queries = [[1, 1], [1, 2], [1, 2], [2, 2], [0, 2], [0, 2]]
    res = isZeroArray(nums, queries)
    print(f"res is {res}")
    assert res is False


tests()
