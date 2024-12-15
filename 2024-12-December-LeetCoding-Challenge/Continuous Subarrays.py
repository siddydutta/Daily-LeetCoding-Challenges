from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        freq = {}
        left, right = 0, 0
        count = 0

        while right < len(nums):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            count += (right - left + 1)
            right += 1

        return count


def main():
    nums = [5, 4, 2, 4]
    assert Solution().continuousSubarrays(nums) == 8

    nums = [1, 2, 3]
    assert Solution().continuousSubarrays(nums) == 6


if __name__ == '__main__':
    main()
