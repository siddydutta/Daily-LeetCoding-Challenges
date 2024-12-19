from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count, curr_max = 0, 0
        for i in range(len(arr)):
            curr_max = max(curr_max, arr[i])
            if curr_max == i:
                count += 1
        return count


def main():
    arr = [4, 3, 2, 1, 0]
    assert Solution().maxChunksToSorted(arr) == 1

    arr = [1, 0, 2, 3, 4]
    assert Solution().maxChunksToSorted(arr) == 4


if __name__ == '__main__':
    main()
