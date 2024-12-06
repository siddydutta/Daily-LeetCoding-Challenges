from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        s, count = 0, 0
        for i in range(1, n+1):
            if i not in banned:
                if s+i > maxSum:
                    return count
                count += 1
                s += i
        return count


def main():
    banned = [1, 6, 5]
    n = 5
    maxSum = 6
    assert Solution().maxCount(banned, n, maxSum) == 2

    banned = [1, 2, 3, 4, 5, 6, 7]
    n = 8
    maxSum = 1
    assert Solution().maxCount(banned, n, maxSum) == 0

    banned = [11]
    n = 7
    maxSum = 50
    assert Solution().maxCount(banned, n, maxSum) == 7


if __name__ == '__main__':
    main()
