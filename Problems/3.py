'''
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price
of a given stock on the ith day.

You want to maximize your profit by choosing a single day to
buy one stock and choosing a different day in the future to
sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because
you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the
max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''


def max_profit(arr) -> int:
    profit = 0
    buy = arr[0]
    print(f"buying at {buy}")
    sell = None
    for item in arr[1:len(arr)]:
        sell = item
        print(f"selling at {sell}")
        print(f"profit is {sell - buy}")
        if sell - buy > profit:
            profit = sell - buy
            print(f"profit for buy at {buy} and sell at {sell} is {profit}")
        elif item < buy:
            buy = item
            profit = 0
            print(f"Buying at {buy}, Resetting profit")
    print(f"profit for input {arr} is {profit}")
    return profit


if __name__ == '__main__':
    inp = [7, 1, 5, 3, 6, 4]
    result = max_profit(inp)
    assert result == 5
    inp = [7, 6, 4, 3, 1]
    result = max_profit(inp)
    assert result == 0
    inp = [10, 20, 8, 17, 34, 22, 11, 50]
    result = max_profit(inp)
    assert result == 42
