from math import inf
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = inf, inf
        for price in prices:
            if price < min1:
                min2, min1 = min1, price
            elif price < min2:
                min2 = price
        rem = money - (min1+min2)
        return rem if rem >= 0 else money


def main():
    prices = [1, 2, 2]
    money = 3
    assert Solution().buyChoco(prices, money) == 0

    prices = [3, 2, 3]
    money = 3
    assert Solution().buyChoco(prices, money) == 3


if __name__ == '__main__':
    main()
