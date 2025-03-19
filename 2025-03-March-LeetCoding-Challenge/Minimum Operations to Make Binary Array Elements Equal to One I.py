class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        flips = 0
        for i in range(n - 2):
            if nums[i] == 1:
                continue
            nums[i] ^= 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            flips += 1
        return flips if nums[-2] == 1 and nums[-1] == 1 else -1


def main():
    nums = [0, 1, 1, 1, 0, 0]
    assert Solution().minOperations(nums) == 3

    nums = [0, 1, 1, 1]
    assert Solution().minOperations(nums) == -1


if __name__ == '__main__':
    main()
