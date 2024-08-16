from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        low, high = arrays[0][0], arrays[0][-1]
        max_distance = 0
        for arr in arrays[1:]:
            max_distance = max(max_distance, arr[-1]-low, high-arr[0])
            low = min(low, arr[0])
            high = max(high, arr[-1])
        return max_distance


def main():
    arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
    assert Solution().maxDistance(arrays) == 4

    arrays = [[1], [1]]
    assert Solution().maxDistance(arrays) == 0


if __name__ == '__main__':
    main()
