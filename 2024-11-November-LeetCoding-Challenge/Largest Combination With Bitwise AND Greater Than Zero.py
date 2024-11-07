from typing import List


class Solution:
    MAX_BITS = 24

    def largestCombination(self, candidates: List[int]) -> int:
        max_size = 0
        for shift in range(self.MAX_BITS):
            size = 0
            for num in candidates:
                if (num >> shift) & 1:
                    size += 1
            max_size = max(max_size, size)
        return max_size


def main():
    candidates = [16, 17, 71, 62, 12, 24, 14]
    assert Solution().largestCombination(candidates) == 4

    candidates = [8, 8]
    assert Solution().largestCombination(candidates) == 2


if __name__ == '__main__':
    main()
