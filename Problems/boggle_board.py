from typing import List, Set, Dict

"""
Problem: Boggle Word Finder

Given a 2D grid of characters (the "Boggle board") and a dictionary of
valid words, find all the words from the dictionary that can be formed on
the board.

Rules for forming a word:
1. The word can start on any character tile on the board.
2. Subsequent letters in the word must be in adjacent tiles (horizontally,
   vertically, or diagonally). Each tile has up to 8 neighbors.
3. The same tile cannot be used more than once within a single word.

For example, if the board is:
[ C, A ]
[ T, S ]

And the dictionary is ["CAT", "CAS", "AT"], the valid words are "CAT"
(C -> A -> T) and "CAS" (C -> A -> S). "AT" is also valid.
"""

"""
Core Intuition and Data Structures

The problem is a search for all valid paths on a grid that form words. A
brute-force approach of finding every possible path and then checking it
against the dictionary is too slow due to the massive number of paths.

The key insight is to use the dictionary to guide the search and "prune"
invalid paths early. We do this by combining two concepts:

1. A Trie (Prefix Tree) Data Structure:
   This is the perfect tool for the dictionary. A Trie lets us check if a
   string is a valid word OR a prefix of a valid word in O(L) time, where
   L is the length of the string. If we are building a word like "CAX" and
   the Trie tells us no words start with "CAX", we can stop that search
   path immediately.

   Example Trie for ["CAR", "CARD", "CAT"]:

   (root)
     |
     +-- C -- A -- T* (* = end of a valid word)
              |
              +-- R* -- D*

2. Depth-First Search (DFS) with Backtracking:
   DFS is a natural way to explore all paths from a starting cell. We go
   as deep as possible down one path. When the path ends (either by forming
   a word or by being an invalid prefix), we "backtrack" to explore other
   options.

   To implement this, we use a `visited` grid to ensure we don't use the
   same tile twice in the current word path. The critical step is that
   after exploring all paths from a tile, we un-mark it as visited, so it
   can be used in completely different words that might start elsewhere.
"""


class TrieNode:
    def __init__(
        self,
    ):
        """
        Initializes a TrieNode.
        A trie node is just a pointer to next word, it doesnt contain
        anything in itself, just pointer to its children
        self.children: A dictionary mapping a character to a child TrieNode.
        self.is_end_of_word: A boolean that is True if the path to this
        node represents a complete word.
        """
        self.children: Dict[str:TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        """
        Initializes the Trie data structure
        """
        self.root = TrieNode()

    def insert(self, word: str):
        """
        Insert a word into the Trie data structure
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            # else:
            #     current_node = current_node.children[char]
        # after the end of loop, mark the last word
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        search for a word in Trie Data structure
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        # The entire word path exists, but we must also check if it's marked
        # as a complete word.
        return current.is_end_of_word

    def starts_with(self, prefix: str):
        """
        Checks if there is any word in the trie that starts with
        the given prefix.
        Args:
            prefix: The prefix to check for.
        Returns:
            True if the prefix exists, False otherwise.
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # If we successfully navigated the entire prefix, it exists.
        return True


def dfs(
    current_word, trie_node, board, row, column, found_words, visited=None
):
    """
    perform a depth first search on the board,
    which is basically a graph
    """
    if not visited:
        visited = set()
    char = board[row][column]
    if (row, column) in visited:
        return
    if char not in trie_node.children:
        return
    else:
        current_word += char
        next_trie_node = trie_node.children[char]
    if next_trie_node.is_end_of_word:
        found_words.add(current_word)
    visited.add((row, column))
    directions = [
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (-1, -1),
        (1, -1),
        (1, 1),
    ]
    for row_add, column_add in directions:
        new_row = row + row_add
        new_column = column + column_add
        if new_row < len(board) and new_column < len(board[0]):
            dfs(
                current_word=current_word,
                trie_node=next_trie_node,
                board=board,
                row=new_row,
                column=new_column,
                found_words=found_words,
                visited=visited,
            )
    visited.remove((row, column))


def find_words(board: List[List[str]], words: List[str]) -> Set[str]:
    """
    This is the main function you will implement.
    It should take the board and a list of dictionary words and return a
    set of all the words that can be found on the board.
    """
    trie = Trie()
    for word in words:
        trie.insert(word)
    rows, columns = len(board), len(board[0])
    found_words = set()
    for i in range(rows):
        for j in range(columns):
            dfs(
                current_word="",
                trie_node=trie.root,
                board=board,
                row=i,
                column=j,
                found_words=found_words,
            )
    return found_words


def tests():
    """
    Contains test cases for the Boggle board implementation.
    """
    board1 = [["C", "A", "R"], ["T", "D", "T"], ["S", "E", "F"]]
    dictionary1 = ["CAR", "CARD", "CAT", "ART"]
    found_words = find_words(board1, dictionary1)
    expected = {"CAR", "CARD", "CAT", "ART"}
    print(f"Board 1: Found words: {found_words}")
    assert found_words == expected

    board2 = [
        ["O", "A", "A", "N"],
        ["E", "T", "A", "E"],
        ["I", "H", "K", "R"],
        ["I", "F", "L", "V"],
    ]
    dictionary2 = ["OATH", "PEA", "EAT", "RAIN"]
    found_words = find_words(board2, dictionary2)
    expected = {"OATH", "EAT"}
    print(f"Board 2: Found words: {found_words}")
    assert found_words == expected

    print("\nAll tests passed.")


if __name__ == "__main__":
    tests()
