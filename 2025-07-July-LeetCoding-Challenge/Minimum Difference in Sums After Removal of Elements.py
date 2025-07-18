from heapq import heapify, heappushpop


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        # minimise first array of size n elements
        first = [0] * (n + 1)
        max_heap = [-num for num in nums[:n]]
        heapify(max_heap)
        total = -sum(max_heap)
        first[0] = total
        for i, num in enumerate(nums[n:n * 2], start=1):
            total += num
            total -= -heappushpop(max_heap, -num)
            first[i] = total

        # maxmimise last array of size n elements
        min_heap = nums[n * 2:]
        heapify(min_heap)
        last = sum(min_heap)
        ans = first[n] - last
        for i, num in enumerate(reversed(nums[n:n * 2]), start=1):
            last += num
            last -= heappushpop(min_heap, num)
            ans = min(ans, first[n - i] - last)
        return ans


def main():
    nums = [3, 1, 2]
    assert Solution().minimumDifference(nums) == -1

    nums = [7, 9, 5, 8, 1, 3]
    assert Solution().minimumDifference(nums) == 1


if __name__ == '__main__':
    main()
