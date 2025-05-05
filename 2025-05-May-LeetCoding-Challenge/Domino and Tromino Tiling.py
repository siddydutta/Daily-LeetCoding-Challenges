class Solution:
    MOD = 10**9 + 7

    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5]
        for _ in range(n - 3):
            # recurrence relation: A[i] = 2*A[i-1] + A[i-3]
            dp = (dp[1], dp[2], ((2 * dp[-1] + dp[-3]) % self.MOD))
        return dp[-1] if n > 3 else dp[n - 1]


def main():
    n = 3
    assert Solution().numTilings(n) == 5

    n = 1
    assert Solution().numTilings(n) == 1


if __name__ == '__main__':
    main()
