from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(distance) -> bool:  # two pointers
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if not enough(mid):
                left = mid + 1
            else:
                right = mid
        return left


def main():
    nums = [1, 3, 1]
    k = 1
    assert Solution().smallestDistancePair(nums, k) == 0

    nums = [1, 1, 1]
    k = 2
    assert Solution().smallestDistancePair(nums, k) == 0

    nums = [1, 6, 1]
    k = 3
    assert Solution().smallestDistancePair(nums, k) == 5


if __name__ == '__main__':
    main()
