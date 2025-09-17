'''
Thinking Through the Problem

This is a classic 2D DP problem. We're going to build a 2D table, dp,
where dp[i][j] will store the length of the LCS between the first i
characters of text1 and the first j characters of text2.

Let's think about how to fill a cell dp[i][j]. We need to look at the
characters text1[i-1] and text2[j-1]. (We use i-1 and j-1 because our
DP table will have an extra row and column for base cases, which I'll
explain in a moment).

We have two possibilities:

1. The characters match: text1[i-1] == text2[j-1]
* If they match, then this character is part of our LCS. The length of
the LCS is 1 plus the LCS of the strings without this character. We look
at the solution for the smaller subproblem, which is stored diagonally
at dp[i-1][j-1].
* Recurrence: dp[i][j] = 1 + dp[i-1][j-1]

2. The characters do NOT match: text1[i-1] != text2[j-1]
* If they don't match, we can't include both. The longest common subsequence
  must be the longest one we could find by either:
    * Ignoring the character from text1
      (looking at the result from dp[i-1][j]).
    * Ignoring the character from text2
      (looking at the result from dp[i][j-1]).
* We take the best (maximum) of these two options.
* Recurrence: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

The DP Table

We'll create a grid of size (len(text1) + 1) x (len(text2) + 1). We initialize
it with all zeros. The extra row and column of zeros serve as our base case:
the LCS of any string with an empty string is 0.

The final answer will be the number in the bottom-right corner of the table.

Why the Max() of two substring matches?

Let me clarify with a concrete example, as the term "probability" can be
misleading here. It's not about chance; it's about exploring two
alternative paths and picking the best one.

Let's say our strings are:
text1 = "sea"
text2 = "eat"

Our goal is to find the LCS of "sea" and "eat". We are at the last characters,
'a' and 't'. They do not match.

This means the true LCS of "sea" and "eat" cannot involve both this 'a' and
this 't' at the same time. So, we have to "throw one away" and see which
option gives us a better result.

Option 1: Throw away the `'a'` from `"sea"`.
We are now looking for the LCS of "se" and "eat". Let's assume our DP table
has already solved this subproblem for us. The LCS of "se" and "eat" is "e",
which has a length of 1.

Option 2: Throw away the `'t'` from `"eat"`.
We are now looking for the LCS of "sea" and "ea". Again, we assume the DP
table has already solved this. The LCS of "sea" and "ea" is "ea", which
has a length of 2.

Now, the `max()` comes in.

We have two possibilities for the LCS of our original strings "sea" and "eat":
* The result from Option 1 (length 1).
* The result from Option 2 (length 2).

Since our goal is to find the longest common subsequence, we must choose the
option that yielded the longer result.

max(length from Option 1, length from Option 2)
max(1, 2) gives us 2.

So, we conclude that the LCS for "sea" and "eat" has a length of 2.

The max() function is how we enforce the "longest" part of the problem's name.
When the characters don't match, we are left with two smaller subproblems,
and we are simply saying, "The best we can do for our current problem is the
best we already did for either of those smaller problems." We are building our
optimal solution from previously computed optimal solutions.
'''


def lcs_length(text1: str, text2: str) -> int:
    '''
    Calculates the length of the longest common subsequence of two strings.
    '''
    # initialize the base row with all zeros
    # len(text1) + 1 because we need an extra row for the base case
    # an empty string wont have any LCS, so its length would be 0
    prev_row = [0] * (len(text2) + 1)

    for i in range(1, len(text1) + 1):
        # initialize the current row with all zeros
        # first column has to be 0 anyway because of the assumption above
        current_row = [0] * (len(text2) + 1)
        for j in range(1, len(text2) + 1):
            # if the characters match, add 1 to the lcs count
            if text1[i-1] == text2[j-1]:
                current_row[j] = 1 + prev_row[j-1]
            else:
                current_row[j] = max(prev_row[j], current_row[j-1])
        prev_row = current_row
    return prev_row[-1]


def run_tests():
    """
    A set of test cases to validate the Longest Common Subsequence
    implementation.
    """
    test_cases = [
        ("abcde", "ace", 3),
        ("abc", "def", 0),
        ("AGGTAB", "GXTXAYB", 4),
        ("abc", "", 0),
        ("", "abc", 0),
        ("", "", 0),
        ("pmjghexybyrgzczy", "hafcdqbgncrcbihkd", 4),
        ("abcba", "abc", 3),
        ("sea", "eat", 2)
    ]

    print("Running Longest Common Subsequence tests...")
    print("="*40)

    all_passed = True
    for i, (text1, text2, expected) in enumerate(test_cases):
        try:
            result = lcs_length(text1, text2)

            if result == expected:
                print(f"--- Test Case {i+1}: PASSED ---")
            else:
                all_passed = False
                print(f"--- Test Case {i+1}: FAILED ---")
                print(f"  text1:    '{text1}'")
                print(f"  text2:    '{text2}'")
                print(f"  Expected: {expected}")
                print(f"  Got:      {result}")

            print("-" * 20)

        except Exception as e:
            all_passed = False
            print(f"--- Test Case {i+1}: ERROR ---")
            print(f"  An exception occurred: {e}")
            print("-" * 20)

    print("="*40)
    if all_passed:
        print("Congratulations! All test cases passed!")
    else:
        print("Some test cases failed. Please review your implementation.")


# To run the tests when you execute the file:
if __name__ == "__main__":
    run_tests()
