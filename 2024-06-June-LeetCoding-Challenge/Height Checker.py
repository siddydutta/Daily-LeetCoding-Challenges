from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for h1, h2 in zip(heights, expected):
            count += (h1 != h2)
        return count


def main():
    heights = [1, 1, 4, 2, 1, 3]
    assert Solution().heightChecker(heights) == 3

    heights = [5, 1, 2, 3, 4]
    assert Solution().heightChecker(heights) == 5

    heights = [1, 2, 3, 4, 5]
    assert Solution().heightChecker(heights) == 0


if __name__ == '__main__':
    main()
