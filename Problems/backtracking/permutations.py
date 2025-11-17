'''
Given an array nums of distinct integers, return all
the possible permutations. You can return the answer
in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        required_len = len(nums)
        used = [False] * len(nums)

        def find_permutations(current_combo):
            # Base Case: If the path has the same number of
            # elements as the input, we have found a
            # complete permutation.
            if len(current_combo) == required_len:
                # Append a copy of the path, not the
                # path itself.
                result.append(list(current_combo))
                return
            # Recursive Step: Iterate through ALL numbers
            # to find the next one.
            for i in range(required_len):
                # The crucial check: only proceed if the
                # number at index 'i' has not been used
                # in this path yet.
                if used[i] is True:
                    continue
                # 1. Choose: Add the number to our path
                # and mark it as used.
                current_combo.append(nums[i])
                used[i] = True
                # 2. Explore: Recurse to find the next
                # elements of the permutation.
                find_permutations(current_combo)
                # 3. Un-choose (Backtrack): Remove the
                # number from the path and un-mark it so
                # it can be used in other permutations.
                used[i] = False
                current_combo.pop()
        find_permutations([])
        return result


def tests():
    sol = Solution()

    # Example 1
    nums1 = [1, 2, 3]
    expected1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1],
                 [3, 1, 2], [3, 2, 1]]
    result1 = sol.permute(nums1)
    assert sorted(map(tuple, result1)) == sorted(map(tuple, expected1))
    print("Test Case 1 (nums=[1,2,3]) passed.")

    # Example 2
    nums2 = [0, 1]
    expected2 = [[0, 1], [1, 0]]
    result2 = sol.permute(nums2)
    assert sorted(map(tuple, result2)) == sorted(map(tuple, expected2))
    print("Test Case 2 (nums=[0,1]) passed.")

    # Example 3
    nums3 = [1]
    expected3 = [[1]]
    assert sol.permute(nums3) == expected3
    print("Test Case 3 (nums=[1]) passed.")


if __name__ == "__main__":
    tests()
