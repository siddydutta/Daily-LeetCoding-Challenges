class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            capability = 0
            idx = 0
            while idx < len(nums):
                if nums[idx] <= mid:
                    capability += 1
                    idx += 2
                else:
                    idx += 1
            if capability >= k:
                right = mid
            else:
                left = mid + 1
        return left


def main():
    nums = [2, 3, 5, 9]
    k = 2
    assert Solution().minCapability(nums, k) == 5

    nums = [2, 7, 9, 3, 1]
    k = 2
    assert Solution().minCapability(nums, k) == 2


if __name__ == '__main__':
    main()
