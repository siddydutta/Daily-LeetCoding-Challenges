class Solution:
    def triangleType(self, nums: list[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return 'none'

        if nums[0] == nums[1]:
            if nums[1] == nums[2]:
                return 'equilateral'
            return 'isosceles'
        if nums[1] == nums[2]:
            return 'isosceles'
        return 'scalene'


def main():
    nums = [3, 3, 3]
    assert Solution().triangleType(nums) == 'equilateral'

    nums = [3, 4, 5]
    assert Solution().triangleType(nums) == 'scalene'


if __name__ == '__main__':
    main()
