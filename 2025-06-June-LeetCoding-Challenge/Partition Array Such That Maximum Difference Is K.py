class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        curr_min = nums[0]
        count = 1
        for num in nums[1:]:
            if num - curr_min > k:
                count += 1
                curr_min = num
        return count


def main():
    nums = [3, 6, 1, 2, 5]
    k = 2
    assert Solution().partitionArray(nums, k) == 2

    nums = [1, 2, 3]
    k = 1
    assert Solution().partitionArray(nums, k) == 2

    nums = [2, 2, 4, 5]
    k = 0
    assert Solution().partitionArray(nums, k) == 3


if __name__ == '__main__':
    main()
