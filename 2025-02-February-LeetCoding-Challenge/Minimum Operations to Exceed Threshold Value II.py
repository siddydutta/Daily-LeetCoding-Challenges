from heapq import heapify, heappop, heappush


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapify(nums)
        count = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, x*2 + y)
            count += 1
        return count


def main():
    nums = [2, 11, 10, 1, 3]
    k = 10
    assert Solution().minOperations(nums, k) == 2

    nums = [1, 1, 2, 4, 9]
    k = 20
    assert Solution().minOperations(nums, k) == 4


if __name__ == '__main__':
    main()
