from typing import Dict, List
'''
Design a data structure that supports adding new
words and finding if a string matches any previously
added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure,
it can be matched later.
bool search(word) Returns true if there is any
string in the data structure that matches word or
false otherwise. word may contain dots '.' where
dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord",
"search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],
["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
'''


class WordNode:
    def __init__(self):
        self.children: Dict[str:WordNode] = {}
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = WordNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        return self.search_from(word, current)

    def search_from(self, word, node) -> bool:
        # Base Case:
        # If word_part is empty, it means we have
        # successfully traversed the Trie for all the
        # characters in the original word. The search
        # is only successful if the node we've landed
        # on is marked as the end of a word.
        if not word:
            return node.is_end_of_word
        # Case 1: The character is a wildcard
        char = word[0]
        if char == ".":
            for child in node.children:
                answer = self.search_from(word[1:], node.children[child])
                if answer is True:
                    return True
            return False
        else:
            # Case 2: The character is a normal letter
            if char not in node.children:
                return False
            else:
                return self.search_from(word[1:], node.children[char])

    def get_matching_words(self, word: str) -> List[str]:
        '''
        get all matching words with the search string
        '''
        current = self.root
        result = self.get_matches(current, word, "")
        return result

    def get_matches(self, node, word_part, current_prefix) -> List[str]:
        # if we are end of search string, word_part would be empty
        if not word_part:
            if node.is_end_of_word:
                return [current_prefix]
            else:
                return []
        # else build a match_list and recursively call subscenarios
        all_match_list = []
        first_part = word_part[0]
        rest_of_word = word_part[1:]

        # Case 1, first char is wild card
        if first_part == ".":
            # recursively call all its neighbours to get matches
            for child in node.children:
                all_child_matches = self.get_matches(
                    node.children[child],
                    rest_of_word,
                    current_prefix + child
                )
                all_match_list.extend(all_child_matches)
        else:
            # first char is a normal letter
            matches = self.get_matches(
                node.children[first_part],
                rest_of_word,
                current_prefix + first_part
            )
            all_match_list.extend(matches)
        return all_match_list


def tests():

    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")

    assert not wordDictionary.search("pad")
    print("Search 'pad' -> Expected: False")

    assert wordDictionary.search("bad")
    print("Search 'bad' -> Expected: True")

    assert wordDictionary.search(".ad")
    print("Search '.ad' -> Expected: True")

    assert wordDictionary.search("b..")
    print("Search 'b..' -> Expected: True")

    wordDictionary.addWord("bat")
    wordDictionary.addWord("but")
    wordDictionary.addWord("bud")

    result = wordDictionary.get_matching_words("b..")
    print(f"result for 'b..' is {result}")
    assert sorted(result) == sorted(["bad", "bat", "but", "bud"])

    result = wordDictionary.get_matching_words("b.d")
    print(f"result for 'b.d' is {result}")
    assert sorted(result) == sorted(["bad", "bud"])

    print("\nAll test cases passed.")


if __name__ == "__main__":
    tests()
