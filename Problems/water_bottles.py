'''
You are given two integers numBottles and numExchange.

numBottles represents the number of full water bottles
that you initially have. In one operation, you can
perform one of the following operations:

1. Drink any number of full water bottles turning them
   into empty bottles.
2. Exchange numExchange empty bottles with one full
   water bottle. Then, increase numExchange by one.

Note that you cannot exchange multiple batches of empty
bottles for the same value of numExchange. For example,
if numBottles == 3 and numExchange == 1, you cannot
exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.

Example 1:
See "Problems/water_bottles_1.png"

Input: numBottles = 13, numExchange = 6
Output: 15
Explanation: The table above shows the number of full
water bottles, empty water bottles, the value of
numExchange, and the number of bottles drunk.

Example 2:
See "Problems/water_bottles_2.png"

Input: numBottles = 10, numExchange = 3
Output: 13
Explanation: The table above shows the number of full
water bottles, empty water bottles, the value of
numExchange, and the number of bottles drunk.
'''


def max_bottles_drunk(num_bottles: int, num_exchange: int):
    empty_bottles = 0
    bottles_drunk = 0
    while (num_bottles > 0) or (empty_bottles >= num_exchange):
        if empty_bottles >= num_exchange:
            empty_bottles = empty_bottles - num_exchange
            num_exchange += 1
            num_bottles += 1
        bottles_drunk += num_bottles
        empty_bottles += num_bottles
        num_bottles = 0
    return bottles_drunk


def tests():
    num_bottles = 10
    num_exchange = 3
    res = max_bottles_drunk(num_bottles, num_exchange)
    print(f"max bottles drunk for {num_bottles} bottles and",
          f"{num_exchange} exchanges is {res}")
    assert res == 13

    num_bottles = 13
    num_exchange = 6
    res = max_bottles_drunk(num_bottles, num_exchange)
    print(f"max bottles drunk for {num_bottles} bottles and",
          f"{num_exchange} exchanges is {res}")
    assert res == 15


tests()
