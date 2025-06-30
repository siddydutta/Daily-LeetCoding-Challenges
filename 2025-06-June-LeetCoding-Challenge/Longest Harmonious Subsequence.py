from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = Counter(nums)
        lhs = 0
        for num in freq.keys():
            if num + 1 in freq:
                lhs = max(lhs, freq[num] + freq[num + 1])
        return lhs


def main():
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    assert Solution().findLHS(nums) == 5

    nums = [1, 2, 3, 4]
    assert Solution().findLHS(nums) == 2

    nums = [1, 1, 1, 1]
    assert Solution().findLHS(nums) == 0


if __name__ == '__main__':
    main()
