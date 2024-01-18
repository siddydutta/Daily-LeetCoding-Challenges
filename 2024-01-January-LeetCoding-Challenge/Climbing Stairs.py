class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1, 2]
        for _ in range(2, n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[-1]


def main():
    n = 2
    assert Solution().climbStairs(n) == 2

    n = 3
    assert Solution().climbStairs(n) == 3


if __name__ == '__main__':
    main()
