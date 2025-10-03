'''
Given a string s, return the longest palindromic substring in s. 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

'''


def longest_palindromic_substring_dp(s: str) -> str:
    '''
    Defining State:
    we need to find if given two indices i and j in the
    string s, s[i:j] is a palindrome or not.
    Therefore, our state needs two params i and j, which
    leads to a 2D DP table or matrix.
    Create a n * n grid where n is the length of the string
    Let say, the rows be the starting index i, and
    columns be the ending index j
    Lets call the n * n grid as matrix named dp.
    dp[i][j] would store a boolean value, True if s[i]..s[:j]
    is a palindrome, and False otherwise.

    Recurrence Relationship:
    Formula that connects the problem to its subproblems:
    dp[i][j] = (s[i] == s[j]) and (dp[i+1][j-1])

    Explanation: s[i:j] is a palindrome if first and last
    letters are the same, and the substring after removing
    the first and last elements is also a palindrome.

    Base cases:
    1. 1 character string is always palindrome
    dp[i][i] = True for all i (i inclusive at the end index too)
    2. 2 character string is a palindrome if both characters
    are the same:
    dp[i][i+1] = (s[i] == s[i+1])
    '''
    n = len(s)
    if n < 2:
        return s
    # initialize the matrix with False. Change to True should
    # be explicit
    dp = [[False] * n for _ in range(n)]

    # these variables will store the start
    longest_palindrome_start = 0
    max_len = 1

    # ----- Base Cases -----
    # Case 1: All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    # Case 2: All substrings of length 2 are palindromes,
    # if s[i] == s[i+1]
    for i in range(n-1):
        if s[i] == s[i + 1]:
            dp[i][i+1] = True
            longest_palindrome_start = i
            max_len = 2

    # Case 3: Recurrence relation for lengths 3 and more.
    # 'length' is the length of the substring we are
    # checking in each iteration.
    for length in range(3, n + 1):
        # i is the starting index of the substring
        for i in range(n - length + 1):
            # j is the ending index of the substring
            j = i + length - 1

            # check if the outer chars match and inner
            # substring is a plaindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    max_len = length
                    longest_palindrome_start = i
    return s[longest_palindrome_start: longest_palindrome_start + max_len]


# Helper function to perform the expansion
def expand_around_center(s: str, left: int, right: int):
    n = len(s)
    max_len = 0
    start = 0
    while left >= 0 and right < n and s[left] == s[right]:
        current_length = right - left + 1
        if current_length > max_len:
            max_len = current_length
            start = left
        left -= 1
        right += 1
    return start, max_len


def longest_palindromic_substring_optimised(s: str) -> str:
    '''
    Intuition: The "Expand from Center" Algorithm
    The core idea is that a palindrome is symmetrical around
    a central point. Instead of checking every possible
    substring to see if it's a palindrome (which is slow),
    we can flip the problem around: assume every possible
    position is the center of a palindrome and expand
    outwards to see how long that palindrome can be.

    1. What is a "Center"?
    There are two types of centers for any palindrome:

    . A single character: This is the center for odd-length
    palindromes. In "r a c e c a r", the character 'e' is
    the center.
    . The space between two characters: This is the center
    for even-length palindromes. In "a a b b a a",
    the center is the space between the two 'b's.
    For a string of length n, there are n single-character
    centers and n-1 between-character centers,
    for a total of 2n - 1 possible centers.

    2. The Expansion Process

    Iterate through every character in the string (from
    index i = 0 to n-1). For each character i, treat it as a
    potential center and perform two expansions:
    . Odd-length check: Assume i is the center. Start with two
    pointers, left = i and right = i. Expand outwards.
    . Even-length check: Assume the space between i and i+1 is
    the center. Start with left = i and right = i+1. Expand outwards.

    The "expansion" means you check if s[left] == s[right].
    If they match, you've found a valid palindrome. You then move the
    pointers (left--, right++) and check again. You stop when the
    characters don't match or when you go out of the string's bounds.
    As you expand, you keep track of the longest palindrome you've seen
    so far. After checking all 2n - 1 potential centers, the one you've
    saved will be the answer.
    This guarantees you check every possible palindrome
    without redundant work.
    '''
    n = len(s)
    # Base Cases
    # string of length 1
    if n < 2:
        return s
    # string of length 2
    if n == 2:
        if s[0] == s[1]:
            return s
        else:
            return ""

    start = 0
    max_length = 1

    # iterate through each character as a potential center
    for i in range(n):
        # Case 1 - Odd numbered string
        strt, max_len = expand_around_center(s, i, i)
        if max_len > max_length:
            max_length = max_len
            start = strt
        # Case 2 - Even numbered string
        strt, max_len = expand_around_center(s, i, i + 1)
        if max_len > max_length:
            max_length = max_len
            start = strt

    return s[start: start + max_length]


def tests():
    s = 'babad'
    res = longest_palindromic_substring_dp(s)
    print(f"longest palindromic substring in '{s}' is {res}")
    assert res == 'bab' or res == 'aba'
    s = 'cbbd'
    res = longest_palindromic_substring_dp(s)
    print(f"longest palindromic substring in '{s}' is {res}")
    assert res == 'bb'
    s = 'babad'
    res = longest_palindromic_substring_optimised(s)
    print(f"longest palindromic substring in '{s}' is {res}")
    assert res == 'bab' or res == 'aba'
    s = 'cbbd'
    res = longest_palindromic_substring_optimised(s)
    print(f"longest palindromic substring in '{s}' is {res}")
    assert res == 'bb'
    s = 'abbbbbaracecar'
    res = longest_palindromic_substring_optimised(s)
    print(f"longest palindromic substring in '{s}' is {res}")
    # assert res == 'bb'


tests()
