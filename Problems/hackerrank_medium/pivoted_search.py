'''
Pivoted Search
Given a sorted array of unique integers that has been rotated at an unknown pivot, find the index of a target value or return -1 if not found.

Example

Input:

nums = [1609466400, 1609470000, 1609473600, 1609459200, 1609462800]
target = 1609459200
Output:

3
Explanation:

We perform a binary search on the rotated array:

left=0, right=4, mid=(0+4)//2=2, nums[mid]=1609473600.
nums[left]=1609466400 <= nums[mid], so the left half [indices 0..2] is sorted. Target 1609459200 is not in [1609466400..1609473600], so search in right half: left=mid+1=3.
Now left=3, right=4, mid=(3+4)//2=3, nums[mid]=1609459200, which equals the target. Return index 3.
'''

def searchRotatedTimestamps(nums, target):
    if not nums:
        return -1
    if len(nums) == 1 and nums[0] == target:
        return 0
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # if left half is sorted
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] <= nums[right]:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def tests():
    nums = [4, 5, 6, 7, 1, 2, 3]
    target = 1
    expected = 4
    result = searchRotatedTimestamps(nums, target)
    print(f"result is {result}")
    assert result == expected


tests()