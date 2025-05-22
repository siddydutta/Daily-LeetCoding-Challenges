from heapq import heappop, heappush


class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        queries.sort()  # queries.sort(lambda q: q[0])
        available, assigned = [], []
        count, ptr = 0, 0
        for time in range(len(nums)):
            while assigned and assigned[0] < time:
                heappop(assigned)
            while ptr < len(queries) and queries[ptr][0] <= time:
                heappush(available, -queries[ptr][1])
                ptr += 1
            while len(assigned) < nums[time] and available and -available[0] >= time:
                heappush(assigned, -heappop(available))
                count += 1
            if len(assigned) < nums[time]:
                return -1
        return len(queries) - count


def main():
    nums = [2, 0, 2]
    queries = [[0, 2], [0, 2], [1, 1]]
    assert Solution().maxRemoval(nums, queries) == 1

    nums = [1, 1, 1, 1]
    queries = [[1, 3], [0, 2], [1, 3], [1, 2]]
    assert Solution().maxRemoval(nums, queries) == 2

    nums = [1, 2, 3, 4]
    queries = [[0, 3]]
    assert Solution().maxRemoval(nums, queries) == -1


if __name__ == '__main__':
    main()
