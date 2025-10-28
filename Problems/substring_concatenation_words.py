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


def substring_concat_optimised(
        s: str, words: List[str]
        ) -> List[int]:
    # Edge case: if s, words, or words[0] is empty,
    # we can't find anything.
    if not s or not words or not words[0]:
        return []

    word_len = len(words[0])
    num_words = len(words)
    window_len = word_len * num_words

    # If the string is shorter than the total length
    # of words, no match is possible.
    if len(s) < window_len:
        return []

    # Create the target frequency map of words to find.
    target_counts = Counter(words)
    result_indices = []

    # This outer loop iterates through each possible
    # "reading frame".
    # For word_len = 3, it will run for i=0,
    # i=1, and i=2.
    # This ensures we check for concatenations starting
    # at any possible index.
    for i in range(word_len):
        # 'left' is the starting pointer of the
        # current sliding window.
        left = i
        # 'words_found' counts how many valid words
        # are in the current window.
        words_found = 0
        # 'window_counts' stores the frequency of words
        # in the current window.
        window_counts = Counter()

        # The inner loop slides the window across the
        # string, jumping by word_len.
        # 'j' represents the start of the word being
        # added to the window from the right.
        for j in range(i, len(s) - word_len + 1, word_len):
            # Get the new word entering the window from
            # the right.
            word = s[j:j + word_len]

            # Case 1: The word is a valid word we are
            # looking for.
            if word in target_counts:
                window_counts[word] += 1
                words_found += 1

                # Subcase 1.1: We have too many of this
                # specific word.
                # We must shrink the window from the left
                # until the count is valid again.
                while window_counts[word] > target_counts[word]:
                    leftmost_word = s[left:left + word_len]
                    window_counts[leftmost_word] -= 1
                    words_found -= 1
                    left += word_len

                # Subcase 1.2: The window is full of the
                # correct number of words.
                if words_found == num_words:
                    # We found a valid concatenation,
                    # so add the starting index.
                    result_indices.append(left)

                    # To continue searching, slide the
                    # window forward by one word.
                    # Remove the leftmost word from the
                    # window counts to make space.
                    leftmost_word = s[left:left + word_len]
                    window_counts[leftmost_word] -= 1
                    words_found -= 1
                    left += word_len

            # Case 2: The word is not in our list of
            # target words.
            # This breaks any potential concatenation,
            # so we must reset the window.
            else:
                window_counts.clear()
                words_found = 0
                # Move the window start to the position
                # after this "imposter" word.
                left = j + word_len

    return result_indices


def tests():
    test_cases = [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "good"], [8]),
        # Edge case for string being the exact concatenation
        ("foobar", ["foo", "bar"], [0])
    ]

    print("--- Testing substring_concat (Original) ---")
    for i, (s, words, expected) in enumerate(test_cases):
        res = substring_concat(s, words)
        print(f"Test {i+1}: result for string '{s}' and",
              f"words: {words} is {res}")
        assert sorted(res) == sorted(expected)

    print("\n--- Testing substring_concat_optimised ---")
    for i, (s, words, expected) in enumerate(test_cases):
        res = substring_concat_optimised(s, words)
        print(f"Test {i+1}: result for string '{s}'",
              f"and words: {words} is {res}")
        assert sorted(res) == sorted(expected)


tests()
