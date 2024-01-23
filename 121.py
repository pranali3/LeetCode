from typing import List


def maxProfit(prices: List[int]) -> int:
    # TC: O(n)
    # SC: O(1)
    profit = 0
    buy = prices[0]

    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit
