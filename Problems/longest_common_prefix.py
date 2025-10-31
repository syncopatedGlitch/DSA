from typing import List
'''
Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the
input strings.
'''


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    for i, word in enumerate(strs[0]):
        for other_words in strs[1:]:
            if i >= len(other_words) or other_words[i] != word:
                return strs[0][:i]
    return strs[0]


def tests():
    strs = ["flower", "flow", "flight"]
    res = longest_common_prefix(strs)
    print(f" longest common prefix for list {strs} is {res}")
    assert res == "fl"
    strs = ["dog", "racecar", "car"]
    res = longest_common_prefix(strs)
    print(f" longest common prefix for list {strs} is {res}")
    assert res == ""


tests()
