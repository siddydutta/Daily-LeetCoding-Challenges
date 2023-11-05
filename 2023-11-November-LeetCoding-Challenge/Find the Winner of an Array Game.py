from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner, win_count = arr[0], 0
        for curr in arr[1:]:
            if curr > winner:
                winner = curr
                win_count = 0
            win_count += 1
            if win_count == k:
                break
        return winner


def main():
    arr = [2, 1, 3, 5, 4, 6, 7]
    k = 2
    assert Solution().getWinner(arr, k) == 5

    arr = [3, 2, 1]
    k = 10
    assert Solution().getWinner(arr, k) == 3


if __name__ == '__main__':
    main()
