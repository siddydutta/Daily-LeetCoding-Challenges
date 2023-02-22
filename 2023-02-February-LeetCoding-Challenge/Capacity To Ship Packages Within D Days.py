# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity: int) -> bool:
            curr_days, total = 1, 0
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    curr_days += 1
                    if curr_days > days:
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


def main():
    weights, days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5
    assert Solution().shipWithinDays(weights, days) == 15

    weights, days = [3, 2, 2, 4, 1, 4], 3
    assert Solution().shipWithinDays(weights, days) == 6

    weights, days = [1, 2, 3, 1, 1], 4
    assert Solution().shipWithinDays(weights, days) == 3


if __name__ == '__main__':
    main()
