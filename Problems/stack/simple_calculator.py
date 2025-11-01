"""
Given a string s representing a valid expression,
implement a basic calculator to evaluate it, and
return the result of the evaluation.

Note: You are not allowed to use any built-in
function which evaluates strings as mathematical
expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


def calculator(s: str) -> int:
    result = 0
    sign = 1
    stack = []
    n = len(s)
    i = 0
    operands = {"+", "-"}
    while i < n:
        if s[i] == " ":
            i += 1
            continue
        elif s[i] == "(":
            stack.append([result, sign])
            result = 0
            sign = 1
            i += 1
        elif s[i] == ")":
            prev_result, prev_sign = stack.pop()
            result = prev_result + (prev_sign * result)
            i += 1
        elif s[i] in operands:
            if s[i] == "-":
                sign = -1
            else:
                sign = 1
            i += 1
        else:
            num = ""
            while i < n and s[i].isdigit():
                num += s[i]
                i += 1
            num = int(num)
            result += num * sign
    return result


def tests():
    s = "1 + 1"
    res = calculator(s)
    print(f"result for '{s}' is {res}")
    assert res == 2
    s = " 2-1 + 2 "
    res = calculator(s)
    print(f"result for '{s}' is {res}")
    assert res == 3
    s = "(1+(4+5+2)-3)+(6+8)"
    res = calculator(s)
    print(f"result for '{s}' is {res}")
    assert res == 23
    s = "34456"
    res = calculator(s)
    print(f"result for '{s}' is {res}")
    assert res == 34456


tests()
