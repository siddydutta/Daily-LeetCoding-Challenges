class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_max, suffix_max = [None] * n, [None] * n
        for idx in range(n):
            suffix_idx = n - 1 - idx
            if idx == 0:
                prefix_max[idx] = nums[idx]
                suffix_max[suffix_idx] = nums[suffix_idx]
            else:
                prefix_max[idx] = max(prefix_max[idx-1], nums[idx])
                suffix_max[suffix_idx] = max(suffix_max[suffix_idx+1], nums[suffix_idx])
        max_triplet = 0
        for j in range(1, n-1):
            max_triplet = max(max_triplet, (prefix_max[j-1] - nums[j]) * suffix_max[j+1])
        return max_triplet


def main():
    nums = [12, 6, 1, 2, 7]
    assert Solution().maximumTripletValue(nums) == 77

    nums = [1, 10, 3, 4, 19]
    assert Solution().maximumTripletValue(nums) == 133

    nums = [1, 2, 3]
    assert Solution().maximumTripletValue(nums) == 0


if __name__ == '__main__':
    main()
