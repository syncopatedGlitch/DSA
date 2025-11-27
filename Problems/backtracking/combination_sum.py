from typing import List

'''
Given an array of distinct integers candidates and
a target integer target, return a list of all unique
combinations of candidates where the chosen numbers
sum to target. You may return the combinations in
any order.

The same number may be chosen from candidates an
unlimited number of times. Two combinations are
unique if the frequency of at least one of the chosen
numbers is different.

The test cases are generated such that the number
of unique combinations that sum up to target is less
than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that
2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

'''
'''
The Two Main Challenges

1. Reusing Numbers: Unlike the standard "Combinations"
   problem, you can use the same number multiple times
   (e.g., [2, 2, 3] for a target of 7).
2. Avoiding Duplicate Combinations: Like the "Combinations"
   problem, the order doesn't matter. [2, 2, 3] is the same
   as [2, 3, 2], so you should only generate it once.

This means we need a strategy that allows for reuse
but prevents reordering.

The Intuition: A Modified "Combinations" Approach

The best way to think about this is to start with the
template for the "Combinations" problem and make one
critical tweak.

Recall how we solved the duplicate combination issue in
that problem: we used a `start` index. By deciding that
we can only pick numbers at or after the start index,
we enforced an ascending order and naturally prevented
duplicates. For example, if we picked 2, we would only
look for numbers 2 and greater for the next choice,
never going back to 1.

We can use that exact same start index strategy here
to solve Challenge #2.

Now, how do we solve Challenge #1 (reusing numbers)
at the same time?

This is the beautiful part. It's a one-character change
in the recursive call.

* In "Combinations" (where you can't reuse numbers),
  after we chose candidates[i], we explored from the
  next index:
    backtrack(..., i + 1)

* In "Combination Sum" (where you can reuse numbers),
  after we choose candidates[i], we want to allow
  ourselves to choose candidates[i] again. So, we explore
  from the same
    index:
    backtrack(..., i)

By passing i instead of i + 1 to the next recursive call,
you are essentially saying:
"I've just picked the number candidates[i]. For the next
choice, I am allowed to pick candidates[i] again, or any
number after it."

When you are finally done picking candidates[i] for a
given path, the for loop will naturally increment to
i + 1, and you will move on to considering the next
candidate in the list.

Walkthrough: candidates = [2, 3, 6], target = 7

Let's define our function:
backtrack(remaining_target, path, start_index)

1. Initial Call: backtrack(7, [], 0)

2. `backtrack(7, [], 0)` is called:
    * Loop i from start_index=0.
    * i = 0 (candidate is 2):
        * Choose: Pick 2. path is [2]. target is now 5.
        * Explore: Call backtrack(5, [2], 0). <-- We pass `i=0` again!
            * `backtrack(5, [2], 0)` is called:
                * Loop j from start_index=0.
                * j = 0 (candidate is 2):
                    * Choose: Pick 2. path is [2, 2]. target is 3.
                    * Explore: Call backtrack(3, [2, 2], 0).
                        * ... eventually this path will try 2
                              (too big) and then 3.
                        * It will find the combination [2, 2, 3].
                    * Un-choose: path becomes [2, 2].
                * j = 1 (candidate is 3):
                    * Choose: Pick 3. path is [2, 3]. target is 2.
                    * Explore: Call backtrack(2, [2, 3], 1).
                        * This will fail to find a solution because
                          it can only start from index 1 (3), which
                          is too big.
                    * Un-choose: path becomes [2].
            * Un-choose: path becomes [2].
    * Un-choose: path becomes [].

The for loop continues, and i becomes 1 (candidate 3),
and the whole process repeats.

Summary of the Intuition

The solution is a clever modification of the standard
backtracking pattern for combinations:

1. Use a `start` index in your loop to ensure you only
   move forward in the candidates array. This prevents
   duplicate combinations (like [3, 2] after you've already
   processed [2, 3]).
2. Pass the *same* `start` index (`i`) to the recursive call.
   This is the key that "unlocks" the ability to reuse the
   current number as many times as you want.
'''


class Solution:
    def combinationSum(
            self,
            candidates: List[int],
            target: int
    ) -> List[List[int]]:
        result = []
        # sort the array so you can stop when you
        # reach the element that is greater than the
        # target sum and break out of recursion loop
        candidates = sorted(candidates)

        def backtracking(current_combo, remaining_target, start_index):
            # base case: append a copy, not original
            if remaining_target == 0:
                result.append(list(current_combo))
                return
            for i in range(start_index, len(candidates)):
                if candidates[i] > remaining_target or candidates[i] > target:
                    break
                # key optimization. See comment in the
                # main function
                # if candidates[i] > target:
                #     break
                current_combo.append(candidates[i])
                # pass i into the backtracking method
                # that allows to use same number multiple
                # times
                backtracking(
                    current_combo,
                    remaining_target - candidates[i],
                    i)
                current_combo.pop()

        backtracking([], target, 0)
        return result


def tests():
    sol = Solution()

    # Example 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    expected1 = [[2, 2, 3], [7]]
    result1 = sol.combinationSum(candidates1, target1)
    sorted_result1 = sorted(map(sorted, result1))
    sorted_expected1 = sorted(map(sorted, expected1))
    print(f"sorted result1 is {sorted_result1}")
    assert sorted_result1 == sorted_expected1
    print("Test Case 1 (candidates=[2,3,6,7], target=7) passed")

    # Example 2
    candidates2 = [2, 3, 5]
    target2 = 8
    expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result2 = sol.combinationSum(candidates2, target2)
    sorted_result2 = sorted(map(sorted, result2))
    sorted_expected2 = sorted(map(sorted, expected2))
    print(f"sorted result2 is {sorted_result2}")
    assert sorted_result2 == sorted_expected2
    print("Test Case 2 (candidates=[2,3,5], target=8) passed")

    # Example 3
    candidates3 = [2]
    target3 = 1
    expected3 = []
    result3 = sol.combinationSum(candidates3, target3)
    print(f"result 3 is {result3}")
    assert result3 == expected3
    print("Test Case 3 (candidates=[2], target=1) passed")


if __name__ == "__main__":
    tests()
