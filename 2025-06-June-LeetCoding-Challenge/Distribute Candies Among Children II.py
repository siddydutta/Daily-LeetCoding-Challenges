class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for i in range(min(limit, n) + 1):
            if n - i <= limit * 2:
                count += min(n - i, limit) - max(0, n - i - limit) + 1
        return count


def main():
    n = 5
    limit = 2
    assert Solution().distributeCandies(n, limit) == 3

    n = 3
    limit = 3
    assert Solution().distributeCandies(n, limit) == 10


if __name__ == '__main__':
    main()
