from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)
        dp_current = [0] * N
        dp_previous = [0] * N

        for i in range(N-1, -1, -1):
            total = stones[i]
            dp_current, dp_previous = dp_previous, dp_current
            for j in range(i+1, N):
                total += stones[j]
                dp_current[j] = max(total - stones[i] - dp_previous[j],
                                    total - stones[j] - dp_current[j-1])

        return dp_current[-1]


if __name__ == '__main__':
    obj = Solution()
    stones = [5, 3, 1, 4, 2]
    assert obj.stoneGameVII(stones) == 6

    stones = [7, 90, 5, 1, 100, 10, 10, 2]
    assert obj.stoneGameVII(stones) == 122
