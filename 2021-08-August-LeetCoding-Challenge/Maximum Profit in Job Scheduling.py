# -*- coding: utf-8 -*-
from bisect import bisect
from typing import List


class Solution:
    ''' 
    Using binary search and dynamic programming.
    Time Complexity: O(nlogn)
    '''
    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profits: List[int]) -> int:
        # Zip all the jobs and sort by their end times
        jobs = sorted(zip(startTime, endTime, profits), key=lambda job: job[1])
        dp_end_time = [0]  # End time memoization
        dp_profit = [0]  # Profit memoization

        for start, end, profit in jobs:
            # Get the index where we can start current job
            index = bisect(dp_end_time, start) - 1  # To replace job
            # If we do current job, compute profit
            current_profit = dp_profit[index] + profit
            if current_profit > dp_profit[-1]:
                # Store job details as profit increases on doing job
                dp_end_time.append(end)
                dp_profit.append(current_profit)

        return dp_profit[-1]  # Max profit


def main():
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    assert Solution().jobScheduling(startTime, endTime, profit) == 120

    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]
    assert Solution().jobScheduling(startTime, endTime, profit) == 150

    startTime = [1, 1, 1]
    endTime = [2, 3, 4]
    profit = [5, 6, 4]
    assert Solution().jobScheduling(startTime, endTime, profit) == 6


if __name__ == '__main__':
    main()

        
