from typing import List
'''
Given an unsorted array of integers nums,
return the length of the longest consecutive
elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements
sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:

Input: nums = [1,0,1,2]
Output: 3
'''

'''
 The "Consume As You Go" Strategy

Instead of iterating through every number, what if we grab
one number, find its entire consecutive sequence, and then
"consume" (remove) all its members from the set so we never
have to look at them again?

The Intuition:

1. Start by putting all numbers into a hash set, just like
   before.
2. Instead of looping through the numbers, loop while the
   set is not empty.
3. Inside the loop, pop an arbitrary number from the set.
   This number is part of some consecutive sequence. You
   don't know where in the sequence it is (start, middle,
   or end).
4. From this number, expand in both directions:
    * Search downwards: Check for num - 1, num - 2, etc.
      As you find them in the set, keep counting and,
      crucially, remove them from the set.
    * Search upwards: Check for num + 1, num + 2, etc.
      Again, as you find them, keep counting and remove
      them from the set.
5. The total length is the sum of numbers you found going
   down, going up, plus the one you started with. Compare
   this to your max length found so far.
6. Now, the outer loop continues. Since you've removed all
   the elements of the sequence you just processed, the
   next number you pop is guaranteed to be from a completely
   different, undiscovered sequence.

Why is this more efficient?

The main loop no longer runs n times. It only runs once
for each disjoint consecutive sequence in the input.

If your input is [1, 2, ..., 1,000,000, 2,000,000]:
* The standard approach loops 1,000,001 times.
* This "consume as you go" approach will loop only twice.
  The first time, it will find and consume the entire
  1...1,000,000 sequence. The second time, it will find
  and consume the 2,000,000.

This ensures that every number is touched only a small,
constant number of times in total, which can be enough
to pass those very strict time limits.
'''


def longest_consecutive_sequence(nums: List) -> int:
    number_set = set(nums)
    total_nums = len(number_set)
    longest_sequence = 0
    for i in nums:
        if i - 1 not in number_set:
            sequence_length = 1
            for j in range(1, total_nums):
                if i + j not in number_set:
                    break
                sequence_length += 1
            longest_sequence = max(sequence_length, longest_sequence)
    return longest_sequence


def longest_consecutive_sequence_optimized(nums: List) -> int:
    number_set = set(nums)
    longest_sequence = 0
    while number_set:
        num = number_set.pop()
        current_length = 1
        # find the sequence downwards
        down_num = num - 1
        while down_num in number_set:
            current_length += 1
            number_set.remove(down_num)
            down_num -= 1

        # find the sequence upwards
        up_num = num + 1
        while up_num in number_set:
            current_length += 1
            number_set.remove(up_num)
            up_num += 1

        longest_sequence = max(current_length, longest_sequence)
    return longest_sequence


def tests():
    nums = [100, 4, 200, 1, 3, 2]
    res = longest_consecutive_sequence_optimized(nums)
    print(f"longest consecutive sequence for {nums} is {res}")
    assert res == 4
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    res = longest_consecutive_sequence_optimized(nums)
    print(f"longest consecutive sequence for {nums} is {res}")
    assert res == 9
    nums = [1, 0, 1, 2]
    res = longest_consecutive_sequence_optimized(nums)
    print(f"longest consecutive sequence for {nums} is {res}")
    assert res == 3
    nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    res = longest_consecutive_sequence_optimized(nums)
    print(f"longest consecutive sequence for {nums} is {res}")
    assert res == 7
    num1 = [i for i in range(1, 25001)]
    num2 = [0 for _ in range(25000)]
    num1.extend(num2)
    nums = num1
    res = longest_consecutive_sequence_optimized(nums)
    print(f"longest consecutive sequence for inp arr is {res}")
    # assert res == 7


tests()
