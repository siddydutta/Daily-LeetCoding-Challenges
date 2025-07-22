class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        left_ptr, right_ptr = 0, 0
        max_score, curr_score, elements = 0, 0, set()

        while left_ptr < n and right_ptr < n:
            if nums[right_ptr] not in elements:
                curr_score += nums[right_ptr]
                max_score = max(max_score, curr_score)
                elements.add(nums[right_ptr])
                right_ptr += 1
            else:
                curr_score -= nums[left_ptr]
                elements.remove(nums[left_ptr])
                left_ptr += 1

        return max_score


def main():
    nums = [4, 2, 4, 5, 6]
    assert Solution().maximumUniqueSubarray(nums) == 17

    nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    assert Solution().maximumUniqueSubarray(nums) == 8


if __name__ == '__main__':
    main()
