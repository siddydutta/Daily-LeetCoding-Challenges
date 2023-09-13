from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(0, n-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = max(candies[i]+1, candies[i+1])

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1]+1, candies[i])

        return sum(candies)


def main():
    ratings = [1, 0, 2]
    assert Solution().candy(ratings) == 5

    ratings = [1, 2, 2]
    assert Solution().candy(ratings) == 4


if __name__ == '__main__':
    main()
