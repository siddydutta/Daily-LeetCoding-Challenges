from collections import defaultdict


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        n = len(nums)
        map1, map2 = defaultdict(int), defaultdict(int)
        for num in nums:
            map2[num] += 1

        for idx, num in enumerate(nums):
            map1[num] += 1
            map2[num] -= 1
            if map1[num] * 2 > idx + 1 and map2[num] * 2 > n - idx - 1:
                return idx
        return -1


def main():
    nums = [1, 2, 2, 2]
    assert Solution().minimumIndex(nums) == 2

    nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
    assert Solution().minimumIndex(nums) == 4

    nums = [3, 3, 3, 3, 7, 2, 2]
    assert Solution().minimumIndex(nums) == -1


if __name__ == '__main__':
    main()
