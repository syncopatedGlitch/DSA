from typing import List
from collections import deque
'''
A transformation sequence from word beginWord to
word endWord using a dictionary wordList is a
sequence of words beginWord -> s1 -> s2 -> ... -> sk
such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that
beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a
dictionary wordList, return the number of words
in the shortest transformation sequence from
beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence
is "hit" -> "hot" -> "dot" -> "dog" -> cog", which
is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList,
therefore there is no valid transformation sequence.

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''


class Solution:
    def ladderLength(
            self,
            beginWord: str,
            endWord: str,
            wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0
        self.wordlist_set = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, ladder_count = queue.popleft()
            if word == endWord:
                return ladder_count
            for neighbour in self.one_char_diff_neighbours(word):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, ladder_count + 1))
        return 0

    def one_char_diff_neighbours(self, word):
        list_of_word_chars = list(word)
        neighbours = []
        for i in range(len(list_of_word_chars)):
            orig_char = list_of_word_chars[i]
            for code in range(ord('a'), ord('z') + 1):
                new_char = chr(code)
                if new_char == orig_char:
                    continue
                list_of_word_chars[i] = new_char
                new_word = "".join(list_of_word_chars)
                if new_word in self.wordlist_set:
                    neighbours.append(new_word)
            list_of_word_chars[i] = orig_char
        return neighbours


def tests():
    sol = Solution()

    # Example 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    res1 = sol.ladderLength(beginWord1, endWord1, wordList1)
    print(f"res1 is {res1}")
    assert res1 == 5
    print("Test Case 1 passed.")

    # Example 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    assert sol.ladderLength(beginWord2, endWord2, wordList2) == 0
    print("Test Case 2 passed.")


if __name__ == "__main__":
    tests()
