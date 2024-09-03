from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, c in enumerate(chalk):
            if c > k:
                return i
            else:
                k -= c
        return None


def main():
    chalk = [5, 1, 5]
    k = 22
    assert Solution().chalkReplacer(chalk, k) == 0

    chalk = [3, 4, 1, 2]
    k = 25
    assert Solution().chalkReplacer(chalk, k) == 1


if __name__ == '__main__':
    main()
