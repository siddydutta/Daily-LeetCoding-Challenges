from bisect import bisect_right
from functools import lru_cache


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort()
        start_times = [start for start, end, value in events]

        @lru_cache(None)
        def dp(idx: int, k: int) -> int:
            if k == 0 or idx == len(events):
                return 0
            next_event_idx = bisect_right(start_times, events[idx][1])
            return max(dp(idx + 1, k), dp(next_event_idx, k - 1) + events[idx][2])

        return dp(0, k)


def main():
    events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
    k = 2
    assert Solution().maxValue(events, k) == 7

    events = [[1, 2, 4], [3, 4, 3], [2, 3, 10]]
    k = 2
    assert Solution().maxValue(events, k) == 10

    events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
    k = 3
    assert Solution().maxValue(events, k) == 9


if __name__ == '__main__':
    main()
