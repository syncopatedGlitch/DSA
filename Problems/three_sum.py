from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        self.nums = nums
        print(f"nums are {self.nums}")
        result = []
        for i in range(len(self.nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -self.nums[i]
            left = i + 1
            right = len(self.nums) - 1
            while left < right:
                sum = self.nums[left] + self.nums[right]
                if sum == target:
                    triplet = [self.nums[i], self.nums[left], self.nums[right]]
                    result.append(triplet)
                    left = self.move_left_pointer(left)
                    right = self.move_right_pointer(right)
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
        return result

    def move_left_pointer(self, left):
        left += 1
        while left < len(self.nums) - 1 and\
                self.nums[left] == self.nums[left - 1]:
            left += 1
        return left

    def move_right_pointer(self, right):
        right -= 1
        while right >= 1 and self.nums[right] == self.nums[right + 1]:
            right -= 1
        return right


def tests():
    nums = [-1, 0, 1, 2, -1, -4]
    c = Solution()
    res = c.threeSum(nums)
    print(f"res is {res}")
    assert res == [[-1, -1, 2], [-1, 0, 1]]
    nums = [2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]
    c = Solution()
    res = c.threeSum(nums)
    print(f"res is {res}")
    a = [[-10, 5, 5], [-5, 0, 5], [-4, 2, 2], [-3, -2, 5], [-3, 1, 2],
         [-2, 0, 2]]
    assert res == a


tests()
