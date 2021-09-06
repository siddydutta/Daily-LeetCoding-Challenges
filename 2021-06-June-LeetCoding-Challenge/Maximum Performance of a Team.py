# -*- coding: utf-8 -*-
from typing import List
from bisect import insort


class Solution:
    '''
    The performance of a team is the sum of their engineers' speeds
    multiplied by the minimum efficiency among their engineers.
    '''
    def maxPerformance(self, n: int, speed: List[int],
                       efficiency: List[int], k: int) -> int:
        # Engineer tuple is (efficiency, speed)
        engineers = list(zip(efficiency, speed))

        # Since efficiency is the multiplication factor, sort by efficiency
        engineers.sort(key=lambda engineer: engineer[0], reverse=True)

        max_performance = int()
        speeds = list()  # Sorted list to maintain top k speeds, to max speeds
        speeds_sum = 0

        # For every loop, e is the minimum efficiency until that stage, and
        # the speed s associated has to be considered while maintaining k.
        for e, s in engineers:
            # If already k engineers considered, remove slowest engineer
            if len(speeds) == k:
                speeds_sum -= speeds.pop(0)
            insort(speeds, s)  # To maintain sorted list
            speeds_sum += s
            max_performance = max(max_performance, speeds_sum * e)
        return max_performance % (10**9 + 7)


if __name__ == '__main__':
    obj = Solution()
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 2
    assert obj.maxPerformance(n, speed, efficiency, k) == 60

    k = 3
    assert obj.maxPerformance(n, speed, efficiency, k) == 68

    k = 4
    assert obj.maxPerformance(n, speed, efficiency, k) == 72
