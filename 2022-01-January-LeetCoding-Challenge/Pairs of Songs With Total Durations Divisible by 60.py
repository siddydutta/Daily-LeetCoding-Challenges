# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class NotSolution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ''' Not the best solution. Time Complexity: O(n) '''
        time = list(map(lambda t: t % 60, time))  # Mod 60 all time values
        # Create map of time: index
        time_index_map = defaultdict(list)
        for idx, t in enumerate(time):
            time_index_map[t].append(idx)

        count = int()
        for idx, t in enumerate(time):
            # If 0, find other 0s, else find target to reach 60
            pairs = time_index_map.get(0, list()) if t == 0 \
                else time_index_map.get(60-t, list())
            # Don't count self index
            count = count+len(pairs)-1 if idx in pairs else count+len(pairs)
        return count // 2  # Since every pair is counted twice


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ''' Better solution based on same concept. Time Complexity: O(n) '''
        time = list(map(lambda t: t % 60, time))  # Mod 60 all time values
        ans, count = 0, [0]*60
        for t in time:
            ans += count[(60-t) % 60]
            count[t] += 1
        return ans


def main():
    time = [30, 20, 150, 100, 40]
    assert Solution().numPairsDivisibleBy60(time) == 3

    time = [60, 60, 60]
    assert Solution().numPairsDivisibleBy60(time) == 3


if __name__ == '__main__':
    main()
