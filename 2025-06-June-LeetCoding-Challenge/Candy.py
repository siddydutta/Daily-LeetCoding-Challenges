class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # every child must have atleast one candy
        # first pass -> going from left to right to satisfy condition
        for i in range(0, n - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = max(candies[i + 1], candies[i] + 1)
        # second pass -> going from right to left to satisfy condition
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


def main():
    ratings = [1, 0, 2]
    assert Solution().candy(ratings) == 5

    ratings = [1, 2, 2]
    assert Solution().candy(ratings) == 4


if __name__ == '__main__':
    main()
