from typing import List
'''
Given an array of strings strs, group the anagrams
together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged
to form "bat". The strings "nat" and "tan" are
anagrams as they can be rearranged to form each
other. The strings "ate", "eat", and "tea" are
anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())


def tests():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = group_anagrams(strs)
    print(f" grouped anagrams for {strs} is {res}")
    # Sort inner lists and then the outer list for a stable comparison
    sorted_res = sorted([sorted(group) for group in res])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    sorted_expected = sorted([sorted(group) for group in expected])
    assert sorted_res == sorted_expected

    strs = [""]
    res = group_anagrams(strs)
    print(f" grouped anagrams for {strs} is {res}")
    assert res == [[""]]

    strs = ["a"]
    res = group_anagrams(strs)
    print(f" grouped anagrams for {strs} is {res}")
    assert res == [["a"]]


tests()
