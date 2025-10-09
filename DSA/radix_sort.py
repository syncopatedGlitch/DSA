'''
Radix sort is a non-comparative sorting algorithm that sorts
numbers by processing individual digits, starting from the
least significant digit (rightmost) and moving toward the
most significant digit (leftmost).

## Core Concept

Instead of comparing entire numbers, radix sort examines each
digit position separately. It uses a stable sorting algorithm
(typically counting sort) to sort numbers based on each digit,
one position at a time.

## Key Insight

The algorithm relies on the fact that if you sort numbers by
their least significant digits first, then by the next digit,
and so on, the final result will be completely sorted.
This works because the stable sorting preserves the relative
order established in previous passes.

## How It Works

1. Determine maximum number of digits: Find the largest number
to know how many passes are needed
    To find the number of passes needed for radix sort, you
    need to determine how many digits are in the largest number.
    Here are the best approaches:
    a. Find the maximum number in the array with a single pass
    b. Count digits in that maximum number: Keep dividing by 10
       until the number becomes 0, count iterations
2. Sort by each digit position: Starting from the rightmost digit
   (units), sort all numbers based on that digit only
3. Use stable sorting: The sorting method must preserve the
   relative order of numbers with the same digit.
4. Move to next digit: Repeat for tens, hundreds, thousands, etc.

## Example

Starting array: [3251, 45, 1232, 999, 12]

Pass 1 - Units digit: [45] → 1:[3251], 2:[1232, 12], 4:[45], 9:[999]
Result: [3251, 1232, 12, 45, 999]

Pass 2 - Tens digit: [3251, 1232, 12, 45, 999] → 1:[12], 3:[1232],
4:[45], 5:[3251], 9:[999]
Result: [12, 1232, 45, 3251, 999]

Pass 3 - Hundreds digit: [12, 1232, 45, 3251, 999] →
0:[12, 45], 2:[1232, 3251], 9:[999]
Result: [12, 45, 1232, 3251, 999]

Pass 4 - Thousands digit: [12, 45, 1232, 3251, 999] →
0:[12, 45, 999], 1:[1232], 3:[3251]
Final result: [12, 45, 999, 1232, 3251]

## Why It Works

The magic happens because of stability. When we sort by the tens
digit, numbers with the same tens digit maintain their relative
order from the units digit sorting. This cascading effect ensures
that by the time we finish with the most significant digit,
all less significant digits are already in correct relative
order.

## Key Characteristics

• **Non-comparative**: Never compares two complete numbers directly
• **Stable**: Equal elements maintain their relative order
• **Linear time**: O(d * n) where d is the number of digits and n is
    the number of elements
• **Space requirement**: Needs additional space for the
    counting/bucket sort
• **Works best with**: Integers, fixed-length strings, or data with
    limited range of values
'''


def radix_sort(arr):
    digits = passes_needed(arr)
    print(f"arr is {arr}")
    # create a stack of 10 indices to store pairs by significant digit
    # Handle edge case where max_num is 0
    if digits == 0:
        digits = 1
    # perform counting sort for each digit position
    for digit_pos in range(digits):
        buckets = [[] for _ in range(10)]
        # find the last number and
        # Step 1: 10 ** digit_pos - Creates the divisor to isolate
        # the desired digit position
        # Step 2: num // (10 ** digit_pos) - Integer division
        # removes all digits to the right
        # Step 3: % 10 - Modulo 10 extracts only the rightmost
        # digit of the result
        for num in arr:
            # The ** operator in Python is the exponentiation
            # operator (power operator). It raises a number to a power
            # 2 ** 3        # 8 (2 to the power of 3)
            # 5 ** 2        # 25 (5 squared)
            digit = (num // (10 ** digit_pos)) % 10
            buckets[digit].append(num)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
    return arr


def passes_needed(arr):
    max_number = max(arr)
    digits = 0
    while max_number > 0:
        max_number = max_number // 10
        digits += 1
    return digits


if __name__ == '__main__':
    arr = [1223, 342, 45, 6786, 453, 22, 1]
    print(f"sorted array is: {radix_sort(arr)}")
