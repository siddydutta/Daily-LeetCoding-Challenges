from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        count = [1] + [0] * k  # count of remainders
        for num in nums:
            prefix = (prefix + num) % k
            res += count[prefix]
            count[prefix] += 1
        return res


def main():
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    assert Solution().subarraysDivByK(nums, k) == 7

    nums = [5]
    k = 9
    assert Solution().subarraysDivByK(nums, k) == 0


if __name__ == '__main__':
    main()
