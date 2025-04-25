class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        count, prefix = 0, 0
        freqs = {0: 1}
        for num in nums:
            if num % modulo == k:
                prefix = (prefix + 1) % modulo
            target = (prefix - k + modulo) % modulo
            count += freqs.get(target, 0)
            freqs[prefix] = freqs.get(prefix, 0) + 1
        return count


def main():
    nums = [3, 2, 4]
    modulo = 2
    k = 1
    assert Solution().countInterestingSubarrays(nums, modulo, k) == 3

    nums = [3, 1, 9, 6]
    modulo = 3
    k = 0
    assert Solution().countInterestingSubarrays(nums, modulo, k) == 2


if __name__ == '__main__':
    main()
