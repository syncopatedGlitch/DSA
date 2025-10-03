def maxFrequencyElements(nums: list) -> int:
    max_freq = 0
    result = 0
    hash_map = {}
    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
        if hash_map[num] > max_freq:
            # new leader, reset result
            max_freq = hash_map[num]
            result = max_freq
        elif hash_map[num] == max_freq:
            # new contender, add to result
            result += hash_map[num]
    return result


def test():
    nums = [1,2,2,3,1,4]
    res = maxFrequencyElements(nums)
    print(res)

test()