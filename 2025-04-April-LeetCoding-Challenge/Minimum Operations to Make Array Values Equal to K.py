class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        distinct = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                distinct.add(num)
        return len(distinct)


def main():
    nums = [5, 2, 5, 4, 5]
    k = 2
    assert Solution().minOperations(nums, k) == 2

    nums = [2, 1, 2]
    k = 2
    assert Solution().minOperations(nums, k) == -1

    nums = [9, 7, 5, 3]
    k = 1
    assert Solution().minOperations(nums, k) == 4


if __name__ == '__main__':
    main()
