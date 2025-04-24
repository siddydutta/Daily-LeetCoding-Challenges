class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        n, distinct = len(nums), len(set(nums))
        ptr1, freqs, count = 0, {}, 0
        for ptr2 in range(n):
            freqs[nums[ptr2]] = freqs.get(nums[ptr2], 0) + 1
            while len(freqs) == distinct:
                count += n - ptr2
                freqs[nums[ptr1]] -= 1
                if freqs[nums[ptr1]] == 0:
                    del freqs[nums[ptr1]]
                ptr1 += 1
        return count


def main():
    nums = [1, 3, 1, 2, 2]
    assert Solution().countCompleteSubarrays(nums) == 4

    nums = [5, 5, 5, 5]
    assert Solution().countCompleteSubarrays(nums) == 10


if __name__ == '__main__':
    main()
