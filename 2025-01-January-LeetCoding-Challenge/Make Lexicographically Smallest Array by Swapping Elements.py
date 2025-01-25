from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)

        # group elements based on the limit
        groups = [deque([sorted_nums[0]])]
        group_map = {sorted_nums[0]: 0}
        for num in sorted_nums[1:]:
            if abs(num - groups[-1][-1]) <= limit:
                groups[-1].append(num)
            else:
                groups.append(deque([num]))
            group_map[num] = len(groups) - 1

        # replace element with the smallest element in its group
        return [groups[group_map[num]].popleft() for num in nums]


def main():
    nums = [1, 5, 3, 9, 8]
    limit = 2
    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 3, 5, 8, 9]

    nums = [1, 7, 6, 18, 2, 1]
    limit = 3
    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 6, 7, 18, 1, 2]

    nums = [1, 7, 28, 19, 10]
    limit = 3
    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 7, 28, 19, 10]


if __name__ == '__main__':
    main()
