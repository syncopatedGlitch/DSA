'''
Given a string s consisting of words and spaces,
return the length of the last word in the string.

A word is a maximal substring consisting of
non-space characters only.


Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''


def length_last_word(s: str) -> int:
    string_len = len(s)
    length_last_word = 0
    first_word_found = False
    for i in range(string_len - 1, 0, -1):
        if s[i] == " " and not first_word_found:
            continue
        if s[i] == " " and first_word_found:
            break
        else:
            length_last_word += 1
            first_word_found = True
    return length_last_word


def tests():
    s = "Hello World"
    res = length_last_word(s)
    print(f"length of last word in string '{s}' is {res}")
    assert res == 5
    s = "   fly me   to   the moon  "
    res = length_last_word(s)
    print(f"length of last word in string '{s}' is {res}")
    assert res == 4
    s = "luffy is still joyboy"
    res = length_last_word(s)
    print(f"length of last word in string '{s}' is {res}")
    assert res == 6


tests()
