from collections import Counter

'''
Given two strings s and t of lengths m and n
respectively, return the minimum window substring
of s such that every character in t 
(including duplicates) is included in the window.
If there is no such substring, return the empty
string "".

The testcases will be generated such that the
answer is unique. 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC"
includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in
the window. Since the largest window of s only has
one 'a', return empty string.
'''


def minimum_window_substring(s: str, t: str) -> str:
    left = 0
    # Dictionary which holds the frequency
    # of all the characters in t
    t_counts = Counter(t)
    # Number of unique characters in t that
    # must be present in the window
    required = len(t_counts)
    # `formed` is used to keep track of how
    # many unique characters in t are present
    # in the current window in the required frequency.
    formed = 0

    # Dictionary which contains the frequency of
    # characters in the current window.
    window_counts = {}
    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None
    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        # if the char is required, increase the formed count
        if char in t and window_counts[char] == t_counts[char]:
            formed += 1
        # if all the required chars are in window
        # start to shrink the window until its invalid again
        while left <= right and formed == required:
            # record the valid window length and left, right
            # coordinates if minimum that the existing value
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            # window_counts is independently managed from
            # t_counts, so all chars would end up here, just
            # decrement count for all chars before deleting
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in t_counts and\
                    window_counts[left_char] < t_counts[left_char]:
                formed -= 1
            # Move the left pointer ahead, this would help to look
            # for a new window.
            left += 1
    return "" if ans[1] is None else s[ans[1]: ans[2] + 1]


def tests():
    s = "ADOBECODEBANC"
    t = "ABC"
    res = minimum_window_substring(s, t)
    print(f"min window substring for strings '{s}'",
          f"and '{t}' is {res}")
    assert res == "BANC"
    s = "a"
    t = "a"
    res = minimum_window_substring(s, t)
    print(f"min window substring for strings '{s}'",
          f"and '{t}' is {res}")
    assert res == "a"
    s = "a"
    t = "aa"
    res = minimum_window_substring(s, t)
    print(f"min window substring for strings '{s}'",
          f"and '{t}' is {repr(res)}")
    assert res == ""


tests()
