class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        freq = dict()
        ptr, count, result = 0, 0, 0
        for num in nums:
            count += freq.get(num, 0)
            freq[num] = freq.get(num, 0) + 1
            while count >= k:
                freq[nums[ptr]] -= 1
                count -= freq[nums[ptr]]
                ptr += 1
            result += ptr
        return result


def main():
    nums = [1, 1, 1, 1, 1]
    k = 10
    assert Solution().countGood(nums, k) == 1

    nums = [3, 1, 4, 3, 2, 2, 4]
    k = 2
    assert Solution().countGood(nums, k) == 4


if __name__ == '__main__':
    main()
