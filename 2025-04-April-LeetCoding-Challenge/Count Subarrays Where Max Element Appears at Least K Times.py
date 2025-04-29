class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_ = max(nums)
        ptr1, curr, count = 0, 0, 0
        for ptr2 in range(len(nums)):
            curr += nums[ptr2] == max_
            while curr >= k:
                curr -= nums[ptr1] == max_
                ptr1 += 1
            count += ptr1
        return count


def main():
    nums = [1, 3, 2, 3, 3]
    k = 2
    assert Solution().countSubarrays(nums, k) == 6

    nums = [1, 4, 2, 1]
    k = 3
    assert Solution().countSubarrays(nums, k) == 0


if __name__ == '__main__':
    main()
