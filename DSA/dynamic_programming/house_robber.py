'''
You are a robber planning to rob houses along a street. Each house has a
certain amount of money. The only constraint is that you cannot rob two
adjacent houses. Given a list of numbers representing the money in each
house, what is the maximum amount of money you can rob?

Example:
* nums = [1, 2, 3, 1]
* The optimal solution is to rob house 1 (money=1) and house 3 (money=3),
for a total of 1 + 3 = 4.
'''

'''
Identify DP Properties:
* Goal: Find the maximum money you can possibly rob from the entire street.
* Choices: Let's think about what decision you have to make at each house,
  say house i. You have two choices:
    1. Rob `house i`: If you do this, you get money[i]. But you cannot have
       robbed house i-1. This means your total loot would be money[i] plus
       the maximum loot you could have gotten from all houses up to house i-2.
    2. Don't rob `house i`: If you skip house i, your loot is simply the
       maximum you could have gotten from all houses up to house i-1.
* Optimal Substructure: The best you can do at house i is the maximum of
  those two choices. This gives us the recurrence:
    max_loot(i) = max( money[i] + max_loot(i-2),  max_loot(i-1) )
* Overlapping Subproblems: This recurrence depends on previous solutions,
  so it fits the DP pattern.
'''


def street_robber(money_list: list):
    # # handle base cases
    # if len(money) == 1:
    #     return money[0]
    # if len(money) == 2:
    #     return max(money[0], money[1])
    # start the loop
    prev_prev_max = 0
    prev_max = 0
    for money in money_list:
        current_max = max(money + prev_prev_max, prev_max)
        prev_prev_max = prev_max
        prev_max = current_max
    return prev_max


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(f"max loot for {nums} is {street_robber(nums)}")
    nums = [1, 4, 2, 6, 3]
    print(f"max loot for {nums} is {street_robber(nums)}")
    nums = [2, 7, 9, 3, 1]
    print(f"max loot for {nums} is {street_robber(nums)}")
    nums = [1]
    print(f"max loot for {nums} is {street_robber(nums)}")
    nums = [1, 2]
    print(f"max loot for {nums} is {street_robber(nums)}")
    nums = []
    print(f"max loot for {nums} is {street_robber(nums)}")
