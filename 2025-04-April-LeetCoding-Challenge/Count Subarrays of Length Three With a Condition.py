class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        return sum([((nums[i] + nums[i + 2]) * 2) == nums[i + 1]
                    for i in range(len(nums) - 2)])


def main():
    nums = [1, 2, 1, 4, 1]
    assert Solution().countSubarrays(nums) == 1

    nums = [1, 1, 1]
    assert Solution().countSubarrays(nums) == 0


if __name__ == '__main__':
    main()
