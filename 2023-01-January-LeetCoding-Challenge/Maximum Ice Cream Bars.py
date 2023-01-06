# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        while coins > 0 and costs and coins >= costs[0]:
            coins -= costs.pop(0)
            count += 1
        return count


def main():
    costs = [1, 3, 2, 4, 1]
    coins = 7
    assert Solution().maxIceCream(costs, coins) == 4

    costs = [10, 6, 8, 7, 7, 8]
    coins = 5
    assert Solution().maxIceCream(costs, coins) == 0

    costs = [1, 6, 3, 1, 2, 5]
    coins = 20
    assert Solution().maxIceCream(costs, coins) == 6


if __name__ == '__main__':
    main()
