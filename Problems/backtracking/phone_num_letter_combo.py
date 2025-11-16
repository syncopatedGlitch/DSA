from typing import List
'''
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the
number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the
telephone buttons) is given below. Note that 1 does
not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = "2"
Output: ["a","b","c"]
'''
'''
This is a classic combinatorial problem, and the most
common and intuitive way to solve it is with
backtracking, which is often implemented using recursion.

The Core Intuition: Building a Decision Tree

Imagine you have to generate the combinations for the
input "23". You can think of this as making a series
of choices and exploring the consequences. This forms a
"decision tree".

1. First Choice (for digit '2'): You have three possible
paths to take: 'a', 'b', or 'c'.
2. Second Choice (for digit '3'): For each of those
first choices, you have another three paths: 'd', 'e',
or 'f'.

Let's visualize this tree:

                       (start)
                          |
         +----------------+----------------+
         |                |                |
         a                b                c
         |                |                |
     +---+---+        +---+---+        +---+---+
     |   |   |        |   |   |        |   |   |
     d   e   f        d   e   f        d   e   f

The final combinations ("ad", "ae", "af", "bd",
"be", "bf", etc.) are the full paths from the root
of this tree to each of the leaves. The goal of our
algorithm is to explore every one of these paths.

The Backtracking/Recursive Approach

Backtracking is a perfect algorithm for exploring
a decision tree like this. We can define a recursive
function that builds a combination one character at
a time.

Let's define a function, say findCombinations
(index, current_string):
* index: The index of the digit in the input string
we are currently processing (e.g., for "23", index=0
is digit '2', index=1 is digit '3').
* current_string: The combination we have built so
far (e.g., "a", then "ad").

Here's how the function would work:

1. Base Case (The Goal):
    * If current_string has the same length as the
      input digits string, we have successfully built
      a full combination. We add it to our results
      list and stop this path of recursion.

2. Recursive Step (Making a Choice and Exploring):
    * Get the current digit to process based on the index.
    * Get the letters that correspond to that digit
      (e.g., for '2', you get "abc").
    * Loop through each of those letters. For each letter:
        * Choose: Make a choice by appending the letter
          to your current_string.
        * Explore: Make a recursive call to
          findCombinations, advancing the index by one and
          passing along the newly formed current_string.
        * Un-choose (Backtrack): After the recursive call
          returns, you need to "undo" your choice so you
          can try the next letter in the loop. (In many Python
            implementations, this is handled implicitly
            by passing a new string to the recursive call,
            rather than modifying a shared one).
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.digits = digits
        self.required_length = len(digits)
        result = []

        def find_combinations(index, current_string):
            if len(current_string) == self.required_length:
                result.append(current_string)
                return
            # recursive step: get letters for a digit and explore
            possible_letters = self.digits_dict[self.digits[index]]
            for letter in possible_letters:
                find_combinations(index + 1, current_string + letter)

        find_combinations(0, "")
        return result


class OptimisedSolution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.digits = digits
        self.required_length = len(digits)
        result = []
        stack = [(0, "")]  # (index, current_string)
        while stack:
            index, current_string = stack.pop()
            if len(current_string) == self.required_length:
                result.append(current_string)
                continue
            possible_words = self.digits_dict[self.digits[index]]
            for word in possible_words:
                stack.append((index + 1, current_string + word))
        return result


def tests():
    sol = Solution()

    # Example 1
    digits1 = "23"
    expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    result1 = sol.letterCombinations(digits1)
    print(f"result1 is {result1}")
    assert sorted(result1) == sorted(expected1)
    print("Test Case 1 (digits='23') passed")

    # Example 2
    digits2 = "2"
    expected2 = ["a", "b", "c"]
    result2 = sol.letterCombinations(digits2)
    print(f"result2 is {result2}")
    assert sorted(result2) == sorted(expected2)
    print("Test Case 2 (digits='2') passed")

    sol1 = OptimisedSolution()

    # Example 3
    digits1 = "23"
    expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    result3 = sol1.letterCombinations(digits1)
    print(f"result3 is {result3}")
    assert sorted(result3) == sorted(expected1)
    print("Test Case 3 (digits='23') passed")

    # Example 4
    digits2 = "2"
    expected2 = ["a", "b", "c"]
    result4 = sol1.letterCombinations(digits2)
    print(f"result4 is {result4}")
    assert sorted(result4) == sorted(expected2)
    print("Test Case 4 (digits='2') passed")


if __name__ == "__main__":
    tests()
