from typing import List
'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        complement = set()
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if not i+1 >= len(nums):
                for j in range(i + 1, len(nums) - 2):
                    if nums[i] == nums[j]:
                        continue
                    target_2_sum = target - nums[i] - nums[j]
                    left = j + 1 if j+1 < len(nums) else float("-inf")
                    right = len(nums) - 1 if len(nums) - 1 != j+1 else float("inf")
                    while left <= right:
                        if nums[left] == nums[right]:
                            right -= 1
                            continue
                        current_two_sum = nums[left] + nums[right]
                        if current_two_sum == target_2_sum:
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            right -= 1
                        elif current_two_sum < target_2_sum:
                            left += 1
                        else:
                            right -= 1
        return result


def test():
    c = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0
    result = c.fourSum(nums, target)
    print(f"result is {result}")
    expected_list = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    expected = [set(i) for i in expected_list]
    assert set(result) == set(expected)


test()
