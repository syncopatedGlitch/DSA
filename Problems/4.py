'''
122. Best Time to Buy and Sell Stock II
Medium

You are given an integer array prices where prices[i] is the price
of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5),
profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6),
profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit,
so we never buy the stock to achieve the maximum profit of 0.

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
'''


def max_profit(arr) -> int:
    profit = 0
    buy = arr[0]
    print(f"buying at {buy}")
    for item in arr[1:len(arr)]:
        sell = item
        print(f"selling at {sell}")
        print(f"profit is {sell - buy}")
        if sell - buy > 0:
            profit += (sell - buy)
            buy = sell
            print(f"profit for buy at {buy} and sell at {sell} is {profit}")
        elif item < buy:
            buy = item
            print(f"Buying at {buy}")
    print(f"profit for input {arr} is {profit}")
    return profit


if __name__ == '__main__':
    inp = [7, 1, 5, 3, 6, 4]
    result = max_profit(inp)
    assert result == 7
    inp = [1, 2, 3, 4, 5]
    result = max_profit(inp)
    assert result == 4
    inp = [7, 6, 4, 3, 1]
    result = max_profit(inp)
    assert result == 0
