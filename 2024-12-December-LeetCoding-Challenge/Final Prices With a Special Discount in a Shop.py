from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = [price for price in prices]
        stack = []
        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                result[stack.pop()] -= price
            stack.append(idx)
        return result


def main():
    prices = [8, 4, 6, 2, 3]
    assert Solution().finalPrices(prices) == [4, 2, 4, 2, 3]

    prices = [1, 2, 3, 4, 5]
    assert Solution().finalPrices(prices) == [1, 2, 3, 4, 5]

    prices = [10, 1, 1, 6]
    assert Solution().finalPrices(prices) == [9, 0, 1, 6]


if __name__ == '__main__':
    main()
