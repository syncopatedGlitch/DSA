'''
The general idea is always: you have a set of "items" to choose from,
each with a "cost" (like weight) and a "value". You also have a "budget"
(like knapsack capacity). Your goal is to pick the best combination of
items to maximize total value without exceeding your budget.

Problem 5: The 0/1 Knapsack Problem

This is the most common variant. The "0/1" means that for each item,
you have two choices: either you take it (1) or you don't (0). You cannot
take a fraction of an item, and you only have one of each.

The Problem Statement:
You are given:
1. A list of item weights.
2. A list of item values.
3. A maximum knapsack capacity.

Find the maximum total value you can carry in the knapsack.

Example:
* weights = [1, 2, 3]
* values = [6, 10, 12]
* capacity = 5

The best combination is to take the item with weight 2 (value 10) and the
item with weight 3 (value 12). Total weight is 5, and the total value is
10 + 12 = 22.

Thinking Through the Problem (DP Approach)

This is a 2D DP problem. The state dp[i][c] will represent the maximum value
we can achieve using only the first `i` items with a knapsack of capacity `c`.

Now, let's consider each item one by one. For the i-th item, we have two
choices:

1. Don't include item `i`: If we don't take it, then the maximum value we
can get is simply the best we could do with the previous i-1 items at the
same capacity
    c. The value is dp[i-1][c].

2. Include item `i`: We can only do this if its weight is less than or equal
to the current capacity (weights[i-1] <= c). If we take it, its value is
values[i-1] plus the best we could do with the previous i-1 items given the
remaining capacity (c - weights[i-1]). The value is
values[i-1] + dp[i-1][c - weights[i-1]].

The Recurrence Relation

Since we want the maximum possible value, we just take the max() of these
two choices:

dp[i][c] = max( dp[i-1][c],  values[i-1] + dp[i-1][c - weights[i-1]] )

We would build a 2D table of (num_items + 1) x (capacity + 1) and fill
it out. The final answer would be in the bottom-right corner.
'''
'''
Imagine our items are:
* weights = [..., 2] (item 2 has weight 2)
* values = [..., 10] (item 2 has value 10)
* capacity = 5

Let's say we are in the middle of filling our DP table. We are trying
to calculate dp[2][5].

`dp[2][5]` asks: "What is the maximum value I can get using only the first
two items (item1, item2) with a total capacity of 5?"

When we are at this state, we are making a decision specifically about
`item2`.

Option A: We DON'T include `item2`
* If we don't take item2, then the problem is simple: the best we can do is
whatever the best was for the previous items (item1 only) at the same
capacity of 5.
* This value is already stored in dp[1][5].

Option B: We DO include `item2` (The scenario you asked about)

1. Get the item's value: We put item2 in our bag. We immediately get
its value, which is 10.

2. Pay the item's cost: item2 has a weight of 2. This space is now used
up in our knapsack.

3. Calculate remaining capacity: Our knapsack started with a capacity of 5.
After putting item2 in it, the remaining capacity is 5 - 2 = 3.

4. Solve the subproblem: Now we have a smaller knapsack of capacity 3.
What can we fill it with? We can fill it with the best possible combination
of the previous items (item1 only). The maximum value we can get from the
first item with a capacity of 3 is already solved and stored in dp[1][3].

So, the total value for this "include item2" option is:
(value of item2) + (the best we could do with the rest of the items in
the remaining space) 10 + dp[1][3]

The Final Decision for `dp[2][5]`

We now have the results of our two choices:
* Value from Option A (don't include item2): dp[1][5]
* Value from Option B (do include item2): 10 + dp[1][3]

We are trying to maximize value, so we take the max() of these two.

The DP Model (Building a Table of All Possibilities):
The DP approach is different. It doesn't simulate one single "timeline"
of filling the knapsack. Instead, it builds a table of answers to many
different, independent, hypothetical questions.

The state dp[i][c] is the answer to the question:
"If you had a fresh, empty knapsack of capacity `c`, and were only
allowed to use items from the set `{item1, item2, ..., item i}`,
what is the absolute maximum value you could get?"

Let's Revisit `dp[2][5]` with this mindset:

The question we are asking is: "What is the max value using {item1, item2}
with a fresh capacity of 5?"

To answer this, we don't have a "remaining capacity" from a previous step.
We have the full capacity of 5 to work with for this specific subproblem.
Our recurrence relation allows us to look up the answers to even smaller,
independent subproblems that we've already solved:

* Choice 1 (Don't take `item2`): The answer is simply the solution to the
subproblem: "What is the max value using {item1} with a fresh capacity of
5?" This is dp[1][5].

* Choice 2 (Take `item2`): If we take item2 (value 10, weight 2), we get
its value (10) and are left with a new, smaller subproblem: "What is the
max value using {item1} with a fresh capacity of 5 - 2 = 3?" The answer
to this is dp[1][3]. So the total value for this choice is 10 + dp[1][3].

The key is that we are not "decrementing the capacity as we go." We are
solving for every possible capacity c from 0 to max_capacity at every
step i. We are building a comprehensive lookup table of optimal solutions,
not just following one path.

So, when you get to dp[2][5], you are not making a decision based on a
"remaining capacity". You are answering a self-contained question about
a capacity of 5, and the formula simply leverages the fact that the
answers for a capacity of 5 and a capacity of 3 (for the previous items)
have already been optimally solved and are waiting for you in the table.
'''


def solve_knapsack(
        weights: list[int],
        values: list[int],
        capacity: int
) -> int:
    """
    Solves the 0/1 Knapsack problem using space-optimized dynamic programming.
    """
    # weights and values must be equal in length
    if not len(weights) == len(values):
        raise Exception("unequal lists. Invalid input")
    # initialize the prev row and add a padding of 1 to meet the base case
    # which is if there are 0 items or 0 capacity, answer would be 0
    prev_row = [0] * (capacity + 1)
    # start a loop to fill each row in the matrix
    for item in range(1, len(weights) + 1):
        # initialize current row of the iteration with zeros
        # first column in the row woudl anyway be 0
        # because of the base case
        current_row = [0] * (capacity + 1)
        for cap in range(1, capacity + 1):
            # each item is the max of two scenarios:
            # 1. we include the item (but only if it fits the capacity), or
            # we dont include the item
            if weights[item - 1] <= cap:
                current_row[cap] = max(
                    prev_row[cap],
                    values[item - 1] + prev_row[cap - weights[item - 1]]
                )
            else:
                # if the item wont fit in the given capacity,
                # then there no no option but to skip the item
                current_row[cap] = prev_row[cap]
        prev_row = current_row
    return prev_row[-1]


def run_tests():
    """
    A set of test cases to validate the 0/1 Knapsack implementation.
    """
    test_cases = [
        # Test Case 1: Standard case
        {
            "weights": [1, 2, 3],
            "values": [6, 10, 12],
            "capacity": 5,
            "expected": 22  # (item 2 with w=2, v=10) + (item 3 with w=3, v=12)
        },
        # Test Case 2: Another standard case
        {
            "weights": [2, 3, 4, 5],
            "values": [3, 4, 5, 6],
            "capacity": 5,
            "expected": 7  # (item 1 with w=2, v=3) + (item 2 with w=3, v=4)
        },
        # Test Case 3: All items fit
        {
            "weights": [1, 1, 1],
            "values": [10, 20, 30],
            "capacity": 3,
            "expected": 60
        },
        # Test Case 4: No items fit
        {
            "weights": [10, 20, 30],
            "values": [60, 100, 120],
            "capacity": 5,
            "expected": 0
        },
        # Test Case 5: Edge case with empty lists
        {
            "weights": [],
            "values": [],
            "capacity": 5,
            "expected": 0
        },
        # Test Case 6: Edge case with zero capacity
        {
            "weights": [1, 2, 3],
            "values": [6, 10, 12],
            "capacity": 0,
            "expected": 0
        }
    ]

    print("Running 0/1 Knapsack tests...")
    print("="*40)

    all_passed = True
    for i, test in enumerate(test_cases):
        try:
            result = solve_knapsack(
                test["weights"], test["values"], test["capacity"]
            )

            if result == test["expected"]:
                print(f"--- Test Case {i+1}: PASSED ---")
            else:
                all_passed = False
                print(f"--- Test Case {i+1}: FAILED ---")
                print(f"  Input: weights={test['weights']},\
                      values={test['values']}, capacity={test['capacity']}")
                print(f"  Expected: {test['expected']}")
                print(f"  Got:      {result}")

            print("-" * 20)

        except Exception as e:
            import traceback
            all_passed = False
            print(f"--- Test Case {i+1}: ERROR ---")
            print(f"  An exception occurred: {e}")
            traceback.print_exc()
            print("-" * 20)

    print("="*40)
    if all_passed:
        print("Congratulations! All test cases passed!")
    else:
        print("Some test cases failed. Please review your implementation.")


if __name__ == "__main__":
    run_tests()
