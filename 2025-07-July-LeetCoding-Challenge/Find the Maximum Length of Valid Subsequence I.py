class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        n_evens, n_odds = 0, 0
        for num in nums:
            if num & 1 == 0:
                n_evens += 1
            else:
                n_odds += 1

        n_alts, parity = 1, nums[0] & 1
        for num in nums[1:]:
            if num & 1 != parity:
                n_alts += 1
                parity = num & 1
        return max(n_evens, n_odds, n_alts)


def main():
    nums = [1, 2, 3, 4]
    assert Solution().maximumLength(nums) == 4

    nums = [1, 2, 1, 1, 2, 1, 2]
    assert Solution().maximumLength(nums) == 6

    nums = [1, 3]
    assert Solution().maximumLength(nums) == 2


if __name__ == '__main__':
    main()
