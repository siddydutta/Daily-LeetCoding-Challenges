class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ptr1, curr_sum, count = 0, 0, 0
        for ptr2 in range(len(nums)):
            curr_sum += nums[ptr2]
            while curr_sum * (ptr2 - ptr1 + 1) >= k:
                curr_sum -= nums[ptr1]
                ptr1 += 1
            count += (ptr2 - ptr1 + 1)
        return count


def main():
    nums = [2, 1, 4, 3, 5]
    k = 10
    assert Solution().countSubarrays(nums, k) == 6

    nums = [1, 1, 1]
    k = 5
    assert Solution().countSubarrays(nums, k) == 5


if __name__ == '__main__':
    main()
