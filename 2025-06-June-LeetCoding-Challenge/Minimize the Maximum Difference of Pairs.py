class Solution:
    def __can_form_pairs(self, nums: list[int], max_diff: int, p: int) -> bool:
        ptr, count = 0, 0
        while ptr < len(nums) - 1 and count < p:
            if nums[ptr + 1] - nums[ptr] <= max_diff:
                count += 1
                ptr += 2
            else:
                ptr += 1
        return count >= p

    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        result = 0
        while left <= right:
            guess = (left + right) // 2
            if self.__can_form_pairs(nums, guess, p):
                result = guess
                right = guess - 1
            else:
                left = guess + 1
        return result


def main():
    nums = [10, 1, 2, 7, 1, 3]
    p = 2
    assert Solution().minimizeMax(nums, p) == 1

    nums = [4, 2, 1, 2]
    p = 1
    assert Solution().minimizeMax(nums, p) == 0


if __name__ == '__main__':
    main()
