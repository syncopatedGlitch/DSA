from typing import List
'''
Given n pairs of parentheses, write a function to
generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(open_count, closed_count, path):
            # Base Case: If the path is the correct length,
            # we have a valid combination.
            if len(path) == 2 * n:
                result.append(path)
                return

            # Rule 1: We can add an open parenthesis '('
            # only if we haven't used all 'n' of them yet.
            if open_count < n:
                backtracking(
                    open_count + 1,
                    closed_count,
                    path + "("
                )

            # Rule 2: We can add a close parenthesis ')'
            # only if it doesn't exceed the number of
            # open parentheses.
            if closed_count < open_count:
                backtracking(
                    open_count,
                    closed_count + 1,
                    path + ")"
                )

        backtracking(0, 0, "")
        return result


def tests():
    sol = Solution()

    # Example 1
    n1 = 3
    expected1 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    result1 = sol.generateParenthesis(n1)
    print(f"result1 is {result1}")
    assert sorted(result1) == sorted(expected1)
    print("Test Case 1 (n=3) passed.")

    # Example 2
    n2 = 1
    expected2 = ["()"]
    result2 = sol.generateParenthesis(n2)
    print(f"result2 is {result2}")
    assert sorted(result2) == sorted(expected2)
    print("Test Case 2 (n=1) passed.")


if __name__ == "__main__":
    tests()
