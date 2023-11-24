from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins = 0
        while piles:
            piles.pop()
            max_coins += piles.pop()
            piles.pop(0)
        return max_coins


def main():
    piles = [2, 4, 1, 2, 7, 8]
    assert Solution().maxCoins(piles) == 9

    piles = [2, 4, 5]
    assert Solution().maxCoins(piles) == 4

    piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
    assert Solution().maxCoins(piles) == 18


if __name__ == '__main__':
    main()
