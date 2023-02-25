# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    assert Solution().maxProfit(prices) == 5

    prices = [7, 6, 4, 3, 1]
    assert Solution().maxProfit(prices) == 0


if __name__ == '__main__':
    main()
