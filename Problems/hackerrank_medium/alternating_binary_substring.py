'''
Longest Alternating Binary Substring with Limited Flips
Given a binary string s and an integer k, find the
length of the longest substring that can be made
alternating (0101... or 1010...) by flipping at most
k bits.

Example 1

Input:
s = 010101
k = 0

Output: 6

Explanation:
The string '010101' is already alternating. With k = 0
flips allowed, the entire string of length 6 is valid,
so the answer is 6.

Example 2

Input:
s = 1001101
k = 2

Output: 7

Explanation:
We can target the alternating pattern '1010101' over the
full length 7.
Comparing to '1001101', mismatches occur at indices 2 and 3.

Flipping those two bits yields '1010101', so the longest
alternating substring is length 7.

Constraints

0 <= s.length <= 100000
s consists only of characters '0' and '1'
0 <= k <= s.length
'''

'''
1. The Core Realization: Two Separate Problems

The first key insight is that any alternating binary string must follow one of two
possible patterns:

1. Pattern A (starts with 0): 010101...
2. Pattern B (starts with 1): 1010101...

A substring is valid if it can be transformed into either Pattern A or Pattern B with at
most k flips.

Trying to solve for both patterns at the same time is complicated. The crucial
simplification is to realize we can solve the problem independently for each pattern and█
then just take the best result.                                                         █
                                                                                        █
So, the problem breaks down into:                                                       █
                                                                                        █
1. Find the longest substring that can become 0101... with at most k flips.            █
2. Find the longest substring that can become 1010... with at most k flips.            █
3. The final answer is the maximum length found in steps 1 and 2.                      █

2. The Right Tool for the Job: Sliding Window

Now, let's focus on just one of the subproblems: "Find the longest substring that can
become 0101... with at most k flips."

This is a classic "longest substring with a property" problem, which is a perfect fit
for the sliding window technique.

Think of a window, defined by a left and right pointer, moving over the string. We want
to find the largest possible valid window.

* The "Property": The number of characters in the window that don't match the target
    pattern (0101...) is less than or equal to k.
* The "Cost": The number of flips needed is our cost. Our budget is k.

3. How the Sliding Window Works

Let's walk through the logic for Pattern A (`0101...`).
1. Initialize:
    * left = 0 (the left edge of our window)
    * flips_used = 0 (our current cost)
    * max_length = 0

2. Expand the Window:
    * We iterate through the string with a right pointer, from the beginning to the
        end.
    * For each character s[right] we add to the window, we check if it matches our
        target pattern.
    * How do we know the target character?
        * If right is an even index, the target is '0'.
        * If right is an odd index, the target is '1'.
    * If s[right] does not match the target, it's a mismatch. We must use a flip, so we
        increment flips_used.

3. Check the Budget (and Shrink if Necessary):
    * After expanding, we check: if flips_used > k.
    * If we've exceeded our budget, our window is now invalid. We must shrink it from
        the left to make it valid again.
    * We enter a loop that moves the left pointer to the right.                        ▄
    * For each character s[left] we are about to remove from the window, we ask: "Did  █
        this character cause us to use a flip?"                                          █
    * If s[left] was a mismatch with the pattern at the left index, then by removing   █
        it, we get one of our flips back. So, we decrement flips_used.                   █
    * We keep shrinking from the left until flips_used is back within our budget (<=   █
        k).                                                                              █
                                                                                        █
4. Update the Answer:                                                                  ▀
    * After every move of the right pointer (and potential shrinking from the left),
        our current window s[left...right] is guaranteed to be valid.
    * We calculate its length: right - left + 1.
    * We update our answer: max_length = max(max_length, right - left + 1).

4. Putting It All Together: The Full Algorithm

1. Define a helper function solve_for_pattern(target_start_char) that implements the
    sliding window logic described above.
    * This function will calculate the number of mismatches against a pattern that
        starts with target_start_char.
    * For example, if target_start_char is '0', it checks against the 0101... pattern.
    * It returns the max_length found for that specific pattern.
2. Run for both patterns:
    * length1 = solve_for_pattern('0')
    * length2 = solve_for_pattern('1')

3. Return the final result:
    * return max(length1, length2)
'''


def longestAlternatingSubstring(s, k):
    if not s:
        return 0
    if k >= len(s):
        return len(s)

    def find_max_length(start_char, s, k):
        left = 0
        max_length = 0
        flips = 0
        for right, char in enumerate(s):
            expected = expected_char(start_char, right)
            if char != expected:
                flips += 1
            if flips >= k:
                while left < right and flips > k:
                    expected = expected_char(start_char, left)
                    if s[left] != expected:
                        flips -= 1
                    left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

    def expected_char(start_char, index):
        if start_char == "0":
            return str(index % 2)
        else:
            return str((index+1)%2)

    length_pattern_1 = find_max_length("0", s, k)
    length_pattern_2 = find_max_length("1", s, k)
    return max(length_pattern_1, length_pattern_2)


def tests():
    test_cases = [
        # Provided examples
        ("010101", 0, 6),
        ("1001101", 2, 7),

        # Additional test cases
        # All same characters, enough flips to make it fully alternating
        ("11111", 2, 5),

        # All same characters, not enough flips for the whole string
        ("00000", 1, 3),  # Can make "010" from "000"

        # No flips needed for a perfect substring
        ("1101011", 1, 6),  # Can make "101010" from "101011" (s[1:7]) with 1 flip.

        # Empty string
        ("", 5, 0),

        # k is larger than string length
        ("001", 5, 3),

        # Complex case
        ("0110001011", 3, 9) # Can change "011000101" (s[0:9]) to "101010101" with 3 flips.
    ]

    for i, (s, k, expected) in enumerate(test_cases):
        result = longestAlternatingSubstring(s, k)
        print(f"Test Case {i+1}: s='{s}', k={k}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected
        print("-" * 20)
        pass


if __name__ == "__main__":
    tests()
