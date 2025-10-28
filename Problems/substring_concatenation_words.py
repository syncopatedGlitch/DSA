from typing import List
from collections import Counter
'''
You are given a string s and an array of strings words.
All the strings of words are of the same length.

A concatenated string is a string that exactly contains
all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef",
"abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
are all concatenated strings. "acdbef" is not a
concatenated string because it is not the concatenation
of any permutation of words.
Return an array of the starting indices of all the
concatenated substrings in s. You can return the answer
in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]

Explanation:
The substring starting at 0 is "barfoo". It is the
concatenation of ["bar","foo"] which is a
permutation of words.
The substring starting at 9 is "foobar". It is the
concatenation of ["foo","bar"] which is a
permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
Output: []

Explanation:
There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
Output: [6,9,12]

Explanation:
The substring starting at 6 is "foobarthe". It is
the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is
the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is
the concatenation of ["the","foo","bar"].
'''


def substring_concat(s: str, words: List[str]) -> List[int]:
    num_words = len(words)
    word_len = len(words[0])
    window_width = num_words * word_len
    res = []
    _map = Counter(words)
    left = 0
    right = window_width
    while right <= len(s):
        window = s[left: right]
        window_words = [window[i: i + word_len]
                        for i in range(0, len(window), word_len)]
        _window_map = Counter(window_words)
        if _window_map == _map:
            res.append(left)
        left += 1
        right += 1
    return res


def tests():
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    res = substring_concat(s, words)
    print(f"result for string '{s}' and words: {words} is {res}")
    assert res == [0, 9]
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    res = substring_concat(s, words)
    print(f"result for string '{s}' and words: {words} is {res}")
    assert res == []
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    res = substring_concat(s, words)
    print(f"result for string '{s}' and words: {words} is {res}")
    assert res == [6, 9, 12]
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    res = substring_concat(s, words)
    print(f"result for string '{s}' and words: {words} is {res}")
    assert res == [8]


tests()
