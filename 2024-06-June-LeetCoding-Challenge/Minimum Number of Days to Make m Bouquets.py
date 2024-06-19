from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(days: int) -> bool:
            bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    # increment bouquets if k group done
                    bouquets += (flowers+1) // k
                    # group flowers in k
                    flowers = (flowers+1) % k
            return bouquets >= m

        if len(bloomDay) < m*k:
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            # binary search for least days
            mid = left + (right-left)//2
            if feasible(mid):
                # minimize number of days
                right = mid
            else:
                left = mid + 1
        return left


def main():
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    assert Solution().minDays(bloomDay, m, k) == 3

    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 2
    assert Solution().minDays(bloomDay, m, k) == -1

    bloomDay = [7, 7, 7, 7, 12, 7, 7]
    m = 2
    k = 3
    assert Solution().minDays(bloomDay, m, k) == 12


if __name__ == '__main__':
    main()
