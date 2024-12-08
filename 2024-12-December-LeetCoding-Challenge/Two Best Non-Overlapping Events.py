from bisect import bisect
from itertools import accumulate
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        # first sort by value
        events.sort(key=lambda event: event[2], reverse=True)
        # then sort by start times
        events.sort(key=lambda event: event[0])
        start_times = [event[0] for event in events]
        max_val = float('-inf')
        max_indices = accumulate([event[2] for event in events][::-1], max)
        max_indices = list(max_indices)[::-1]

        for _, end, value in events:
            max_val = max(max_val, value)
            index = bisect(start_times, end)
            if index < n:
                max_val = max(max_val, value+max_indices[index])
        return max_val


def main():
    events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
    assert Solution().maxTwoEvents(events) == 4

    events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]
    assert Solution().maxTwoEvents(events) == 5

    events = [[1, 5, 3], [1, 5, 1], [6, 6, 5]]
    assert Solution().maxTwoEvents(events) == 8


if __name__ == '__main__':
    main()
