'''
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''


def generate_parentheses(n: int):
    '''
    Backtracking approach
    This is a classic backtracking problem.
    We build the string character by character,
    and at each step, we have two choices:
    . add an open parenthesis '(' or a close
    parenthesis ')'.
    We follow two rules to ensure the string
    is always well-formed:
    1. We can only add an open parenthesis if
       we haven't used all 'n' of them yet.
    2. We can only add a close parenthesis if
       it doesn't exceed the number of open
       parentheses already placed.
    '''
    result = []
    # This is our recursive helper function.
    # `open_count`: number of open
    # parentheses used so far.
    # `close_count`: number of close
    # parentheses used so far.
    # `current_string`: the string we are
    # currently building.

    def backtrack(
        open_count,
        closed_count,
        current_string
    ):
        # Base case: If the string is complete
        # (length 2*n), we've found a valid combination.
        # Add it to the result and stop this path.
        if len(current_string) == 2*n:
            result.append(current_string)
            return
        if open_count < n:
            backtrack(open_count + 1, closed_count, current_string + "(")

        if closed_count < open_count:
            backtrack(open_count, closed_count + 1, current_string + ")")

    backtrack(0, 0, "")
    return result


def tests():
    n = 3
    res = generate_parentheses(n)
    print(f"valid parentheses combination for number {n} is {res}")
    assert set(res) == {"((()))", "(()())", "(())()", "()(())", "()()()"}
    n = 1
    res = generate_parentheses(n)
    print(f"valid parentheses combination for number {n} is {res}")
    assert res == ["()"]


tests()
