from collections import deque
from itertools import accumulate
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ps = [0] + list(accumulate(nums))
        queue = deque()
        min_length = float('inf')
        for j in range(len(ps)):
            while queue and ps[j] - ps[queue[0]] >= k:
                min_length = min(min_length, j - queue.popleft())
            while queue and ps[j] <= ps[queue[-1]]:
                queue.pop()
            queue.append(j)
        return min_length if min_length != float('inf') else -1


def main():
    nums = [1]
    k = 1
    assert Solution().shortestSubarray(nums, k) == 1

    nums = [1, 2]
    k = 4
    assert Solution().shortestSubarray(nums, k) == -1

    nums = [2, -1, 2]
    k = 3
    assert Solution().shortestSubarray(nums, k) == 3


if __name__ == '__main__':
    main()
