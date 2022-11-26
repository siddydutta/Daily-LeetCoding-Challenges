# -*- coding: utf-8 -*-
from bisect import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profit: List[int]) -> int:
        # sort jobs by their end times
        jobs = sorted(zip(startTime, endTime, profit), key=lambda job: job[1])
        dp_end_time, dp_cost = [0], [0]

        for start, end, cost in jobs:
            # find index where job can be scheduled
            index = bisect(dp_end_time, start) - 1
            current_cost = dp_cost[index] + cost
            if current_cost > dp_cost[-1]:
                dp_end_time.append(end)
                dp_cost.append(current_cost)

        return dp_cost[-1]


def main():
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    assert Solution().jobScheduling(startTime, endTime, profit) == 120

    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    assert Solution().jobScheduling(startTime, endTime, profit) == 150

    startTime = [1, 1, 1]
    endTime = [2, 3, 4]
    profit = [5, 6, 4]
    assert Solution().jobScheduling(startTime, endTime, profit) == 6


if __name__ == '__main__':
    main()
