class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        max_size = 0
        bitwise_and = 0
        ptr1 = 0
        for ptr2 in range(len(nums)):
            while bitwise_and & nums[ptr2]:
                bitwise_and ^= nums[ptr1]
                ptr1 += 1
            bitwise_and |= nums[ptr2]
            max_size = max(max_size, ptr2 - ptr1 + 1)
        return max_size


def main():
    nums = [1, 3, 8, 48, 10]
    assert Solution().longestNiceSubarray(nums) == 3

    nums = [3, 1, 5, 11, 13]
    assert Solution().longestNiceSubarray(nums) == 1


if __name__ == '__main__':
    main()
