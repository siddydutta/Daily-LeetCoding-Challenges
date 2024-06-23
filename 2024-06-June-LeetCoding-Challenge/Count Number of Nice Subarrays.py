from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # count subarrays with sum k after converting to binary array
        ps_counts = {0: 1}
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += (num % 2)
            # for i < j
            # if sum(nums[0:j]) - sum(nums[0:i]) = k
            # then sum(nums[i+1:j]) = k
            result += ps_counts.get(prefix_sum - k, 0)
            ps_counts[prefix_sum] = ps_counts.get(prefix_sum, 0) + 1
        return result


def main():
    nums = [1, 1, 2, 1, 1]
    k = 3
    assert Solution().numberOfSubarrays(nums, k) == 2

    nums = [2, 4, 6]
    k = 1
    assert Solution().numberOfSubarrays(nums, k) == 0


if __name__ == '__main__':
    main()
