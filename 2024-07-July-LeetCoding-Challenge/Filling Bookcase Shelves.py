from math import inf
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [inf] * (n+1)
        # dp[i] represents the minimum height required for the first i books
        dp[0] = 0

        for i in range(1, n+1):
            total_width = 0
            max_height = 0
            for j in range(i, 0, -1):
                width, height = books[j-1]
                total_width += width
                max_height = max(max_height, height)
                if total_width > shelfWidth:
                    break
                dp[i] = min(dp[i], dp[j-1]+max_height)
        return dp[n]


def main():
    books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    shelfWidth = 4
    assert Solution().minHeightShelves(books, shelfWidth) == 6

    books = [[1, 3], [2, 4], [3, 2]]
    shelfWidth = 6
    assert Solution().minHeightShelves(books, shelfWidth) == 4


if __name__ == '__main__':
    main()
