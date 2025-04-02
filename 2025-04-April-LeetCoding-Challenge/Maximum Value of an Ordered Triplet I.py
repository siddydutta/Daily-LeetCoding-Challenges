class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        max_triplet = 0
        diff_max, prod_max = 0, 0
        for num in nums:
            max_triplet = max(max_triplet, diff_max * num)
            diff_max = max(diff_max, prod_max - num)
            prod_max = max(prod_max, num)
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
