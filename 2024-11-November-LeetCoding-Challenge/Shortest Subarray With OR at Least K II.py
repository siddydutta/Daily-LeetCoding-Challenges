from typing import List


class Solution:
    def update_bit(self, bits: List[int], num: int, rem: int) -> int:
        curr = 0
        for i in range(len(bits)):
            bits[~i] += ((num >> i) & 1) * rem
            curr += (bits[~i] > 0) * (2**i)
        return curr

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        bits = [0] * 32
        left = 0
        for right in range(len(nums)):
            curr = self.update_bit(bits, nums[right], 1)
            while curr >= k and left <= right:
                ans = min(ans, right-left+1)
                curr = self.update_bit(bits, nums[left], -1)
                left += 1
        return ans if ans != float('inf') else -1


def main():
    nums = [1, 2, 3]
    k = 2
    assert Solution().minimumSubarrayLength(nums, k) == 1

    nums = [2, 1, 8]
    k = 10
    assert Solution().minimumSubarrayLength(nums, k) == 3

    nums = [1, 2]
    k = 0
    assert Solution().minimumSubarrayLength(nums, k) == 1


if __name__ == '__main__':
    main()
