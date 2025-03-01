class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n, j = len(nums), 0
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


def main():
    nums = [1, 2, 2, 1, 1, 0]
    assert Solution().applyOperations(nums) == [1, 4, 2, 0, 0, 0]

    nums = [0, 1]
    assert Solution().applyOperations(nums) == [1, 0]


if __name__ == '__main__':
    main()
