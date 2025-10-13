'''
Given an integer array nums, return an array answer such
that answer[i] is equal to the product of all the
elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and
without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
'''
Intuition for Solving Without Division

To solve this without division, the key is to think about
what makes up the final product for each element. For any
given number in the array, nums[i], the desired result is
the product of all numbers to its left multiplied by the
product of all numbers to its right.

Let's use your example: nums = [1, 2, 3, 4]

- To find the result for nums[2] (which is 3), you need
  to calculate:
    - The product of everything to its left: 1 * 2 = 2
    - The product of everything to its right: 4
    - The final result is 2 * 4 = 8.

Doing this naively for every element would be slow. However,
you can calculate these "left" and "right" products for all
elements efficiently in just two passes over the array.

1. First Pass (Left to Right): Imagine creating your results
   array. In the first pass, you can iterate from the beginning
   to the end. For each position, you calculate the product of
   all the numbers that have come before it and store that in
   the corresponding position in your results array.

2. Second Pass (Right to Left): Now, iterate from the end of
   the array back to the beginning. This time, keep track of
   the running product of all numbers to the right. As you
   iterate, multiply the value you currently have in your
   results array (which is the "left product" from the first
   pass) by the new "right product" you are tracking in this
   second pass.

By the end of the second pass, each position in your results
array will have been updated with the product of its left
side and its right side, giving you the final answer without
ever using division.

Instead of recalculating the product for each element, you
accumulate it in a single variable during each pass.

* Pass 1 (Left-to-Right):
    You maintain a single variable, say left_product,
    initialized to 1. As you iterate through the array from
    left to right, you do two things at each position i:
    1. First, you set the value of your result array at i
       to the current left_product.
    2. Then, you update left_product by multiplying it with
       the number at i.
    This is one single loop. No inner loop is needed because
    left_product carries the cumulative product from the
    previous elements.

* Pass 2 (Right-to-Left):
    You do the exact same thing but in reverse. You maintain
    a right_product variable, also initialized to 1. As you
    iterate from right to left:
    1. You multiply the existing value in your result array
       (which already holds the left product) by the current
       right_product.
    2. Then, you update right_product by multiplying it with
    the number at that position.
    This is also a single loop.

Since you are making two separate passes through the array
(one from left-to-right and one from right-to-left), the
total number of operations is proportional to n + n, which
is 2n. In Big O notation, we drop the constant, so the final
time complexity is O(n).
'''


def product_of_array_without_div(arr: list) -> list:
    result = []
    # going left to right
    # initialize for first element
    left_product = 1
    result.append(1)
    for i in range(1, len(arr)):
        left_product = left_product * arr[i - 1]
        result.append(left_product)
    # going right to left
    # initialize for first element
    right_product = 1
    for i in range(len(arr) - 1, -1, -1):
        result[i] = result[i] * right_product
        right_product = right_product * arr[i]
    return result


def product_of_array_with_div(arr: list) -> list:
    product = 1
    zero_loc = set()
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_loc.add(i)
        else:
            product = product * arr[i]
    print(f"product is {product}")
    answer = []
    if len(zero_loc) > 1:
        return [0] * len(arr)
    elif len(zero_loc) == 1:
        for i in range(len(arr)):
            if i in zero_loc:
                answer.append(product)
            else:
                answer.append(0)
    else:
        for i in range(len(arr)):
            prod = product / arr[i]
            answer.append(int(prod))
    return answer


def tests():
    inp = [1, 2, 3, 4]
    res = product_of_array_with_div(inp)
    print(f"product of array {inp} with div is {res}")
    assert res == [24, 12, 8, 6]
    inp = [-1, 1, 0, -3, 3]
    res = product_of_array_with_div(inp)
    print(f"product of array {inp} with div is {res}")
    assert res == [0, 0, 9, 0, 0]
    inp = [1, 2, 3, 4]
    res = product_of_array_without_div(inp)
    print(f"product of array {inp} without div is {res}")
    assert res == [24, 12, 8, 6]
    inp = [-1, 1, 0, -3, 3]
    res = product_of_array_without_div(inp)
    print(f"product of array {inp} wihtout div is {res}")
    assert res == [0, 0, 9, 0, 0]

tests()
