# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        ''' Recursive solution. '''
        n = len(arr)
        visited = [False] * n  # Marking indices as visited or not

        def recursive(index, visited):
            if index < 0 or index >= n or visited[index]:
                return False  # Index out of bounds, or already visited

            if arr[index] == 0:
                return True  # Condition required
            visited[index] = True  # Mark index as visited
            # Try both possible moves
            return recursive(index+arr[index], visited) or \
                recursive(index-arr[index], visited)

        return recursive(start, visited)


def main():
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    assert Solution().canReach(arr, start)

    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 0
    assert Solution().canReach(arr, start)

    arr = [3, 0, 2, 1, 2]
    start = 2
    assert not Solution().canReach(arr, start)


if __name__ == '__main__':
    main()
