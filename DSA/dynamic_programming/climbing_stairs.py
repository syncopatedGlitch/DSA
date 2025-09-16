'''You are climbing a staircase that takes n steps to reach the top.
Each time, you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?

Intuition:
1. In How many ways can you climb 1 stair (1 way - 1 step)
2. In how many ways can you climn 2 stairs (2 ways- 1 + 1 step or
    2 steps)
3. In how many ways can you climb n stairs? Since there are only two
    step options, you will either need to be on (n-1)th step to reach
    nth step by taking 1 step, or you need to be on (n-2)th step to
    reach nth step by taking 2 steps.
    So, if num. of ways to reach nth step is ways(n), then
    ways(n) = ways(n-1) + ways(n-2)
    Thats a classic fibonacci sequence problem solvable by dp.
'''
'''
The reason we use 1 for the "0th" step in the climbing stairs problem
is a matter of modeling the problem correctly.

Let's redefine our state: dp[i] = "the number of ways to stand on step i".

* `dp[1]`: How many ways to stand on the 1st step?
    * Just one way: take a single 1-step from the ground. So, dp[1] = 1.

* `dp[2]`: How many ways to stand on the 2nd step?
    * Two ways:
        1. Take a 1-step from step 1.
        2. Take a 2-step from the ground (step 0).
    * So, dp[2] should be (ways to get to step 1) + (ways to get to step 0).
    * dp[2] = dp[1] + dp[0].

We know dp[2] must be 2, and dp[1] is 1. So the math has to be:
2 = 1 + dp[0]. This forces dp[0] to be 1.
'''


def tabulation_stairs(n):
    # base case
    if n <= 1:
        return 1
    # A simple O(n) space solution would use an array,
    # but the best solution uses O(1) space by only keeping track
    # of the last two values.
    prev_prev = 1
    prev = 1
    for _ in range(2, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    return current


if __name__ == '__main__':
    res = tabulation_stairs(6)
    print(res)
