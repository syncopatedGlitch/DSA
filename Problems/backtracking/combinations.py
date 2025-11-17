from typing import List
'''
Given two integers n and k, return all possible combinations
of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1]
are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
'''
'''
The Best Strategy: Enforce Order to Prevent Duplicates

The core intuition is this: If we decide that all our
combinations must be in ascending order, we can't ever
generate a duplicate.

Think about it:
* The combination of 1 and 2 would always be represented
as [1, 2].
* The form [2, 1] would be illegal under this rule, so we
design our algorithm to never even create it.

This simple rule prunes the decision tree and makes the
algorithm much more efficient.

How to Implement This "Ascending Order" Rule

We can enforce this rule by carefully controlling the
starting point of our search at each level of the
recursion.

Let's define a recursive function:
backtrack(start_number, current_combination)

* start_number: The number we should begin our search from.
* current_combination: The list of numbers we've picked so far.

Walkthrough: `n = 4, k = 2`

1. Initial Call: backtrack(1, [])
    * We need to pick the first number. We can start from 1.
    * Our loop will go from i = 1 to 4.

2. Level 1 (i = 1):
    * Choose: Pick 1. current_combination is now [1].
    * Explore: Make a recursive call: backtrack(2, [1]).
        * Crucially, the next start number is `i + 1`
          (which is 2). This is the magic. We are now
          only allowed to pick numbers greater than 1.
        * The inner loop goes from j = 2 to 4.
        * Level 2 (j = 2): Choose 2. current_combination
          is [1, 2]. It has length k. Add `[1, 2]` to
          results. Backtrack.
        * Level 2 (j = 3): Choose 3. current_combination
          is [1, 3]. It has length k. Add `[1, 3]` to
          results. Backtrack.
        * Level 2 (j = 4): Choose 4. current_combination
          is [1, 4]. It has length k. Add `[1, 4]` to results.
          Backtrack.
    * Un-choose: The recursive call for 1 is done.
      We remove 1 from the combination.

3. Level 1 (i = 2):
    * Choose: Pick 2. current_combination is now [2].
    * Explore: Make a recursive call: backtrack(3, [2]).
        * The start number is 3. The loop for the next
          number will only consider 3 and 4. It will never
          consider 1, so [2, 1] is impossible to create!
        * Level 2 (j = 3): Choose 3. current_combination
          is [2, 3]. Add to results.
        * Level 2 (j = 4): Choose 4. current_combination
        is [2, 4]. Add to results.
    * Un-choose: Remove 2.

4. Level 1 (i = 3):
    * Choose: Pick 3. current_combination is [3].
    * Explore: backtrack(4, [3]).
        * Level 2 (j = 4): Choose 4. current_combination
          is [3, 4]. Add to results.
    * Un-choose: Remove 3.

5. Level 1 (i = 4):
    * Choose: Pick 4. current_combination is [4].
    * Explore: backtrack(5, [4]). The loop for i in
      range(5, 5) does nothing, so it returns immediately.

The process finishes, and we have correctly generated only
the unique, sorted combinations.
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = [(1, [])]
        result = []
        while stack:
            start_num, current_combination = stack.pop()
            if len(current_combination) == k:
                result.append(current_combination)
                continue
            for num in range(start_num, n + 1):
                combo = list(current_combination)
                combo.append(num)
                stack.append((num + 1, combo))
        return result


class RecursiveSolution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def find_combo(start_num, current_combo):
            # base case 1: If the current combination has
            # k elements, it's complete.
            if len(current_combo) == k:
                result.append(list(current_combo))
                return
            # Base Case 2 (Pruning): If we've gone past 'n'
            # or if there aren't enough remaining numbers
            # to form a k-sized combination, stop this path.
            # (k - len(current_combo)) is how many more
            # numbers we need.
            # (n - start_num + 1) is how many numbers are
            # available from start_num to n.
            if start_num > n\
                    or (k - len(current_combo)) > (n - start_num + 1):
                return
            for i in range(start_num, n + 1):
                # Choose: Add the current number 'i' to the combination
                current_combo.append(i)
                # This ensures numbers are always increasing, preventing
                # duplicates like [2,1] if [1,2] is found.
                find_combo(i + 1, current_combo)
                # 3. Un-choose (Backtrack): Remove the current number 'i'
                # This allows the loop to try other numbers at the
                # current level.
                current_combo.pop()

        find_combo(1, [])
        return result


def tests():
    sol = Solution()

    # Example 1
    n1, k1 = 4, 2
    expected1 = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    result1 = sol.combine(n1, k1)
    sorted_result1 = sorted([sorted(c) for c in result1])
    sorted_expected1 = sorted([sorted(c) for c in expected1])
    print(f"sorted result1 is {sorted_result1}")
    assert sorted_result1 == sorted_expected1
    print("Test Case 1 (n=4, k=2) passed")

    # Example 2
    n2, k2 = 1, 1
    expected2 = [[1]]
    assert sol.combine(n2, k2) == expected2
    print("Test Case 2 (n=1, k=1) passed")


if __name__ == "__main__":
    tests()
