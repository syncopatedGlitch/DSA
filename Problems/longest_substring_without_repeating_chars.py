'''
Given a string s, find the length of the longest
substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length
of 3. Note that "bca" and "cab" are also correct
answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke"
is a subsequence and not a substring.
'''


def lcs_without_repeating_chars(s: str) -> int:
    left = 0
    seen = set()
    length = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        length = max(length, right - left + 1)
    return length


def tests():
    s = "abcabcbb"
    res = lcs_without_repeating_chars(s)
    print(f"length of lcs for string '{s}' is {res}")
    assert res == 3
    s = "bbbbb"
    res = lcs_without_repeating_chars(s)
    print(f"length of lcs for string '{s}' is {res}")
    assert res == 1
    s = "pwwkew"
    res = lcs_without_repeating_chars(s)
    print(f"length of lcs for string '{s}' is {res}")
    assert res == 3


tests()
