from typing import List


def maxProfit(prices: List[int]) -> int:
    # TC: O(n)

    profit = 0
    if len(prices) < 2:
        return profit

    buy = prices[0]

    for sell in prices[1:]:
        if sell > buy:
            profit += (sell - buy)
        buy = sell
    return profit
