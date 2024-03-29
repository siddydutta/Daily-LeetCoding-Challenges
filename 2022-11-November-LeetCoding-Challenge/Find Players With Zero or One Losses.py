# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, loosers = zip(*matches)
        return list(map(sorted, [set(winners) - set(loosers),
                                 [player for player, count in
                                     Counter(loosers).items() if count == 1]]))


def main():
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9],
               [10, 4], [10, 9]]
    assert Solution().findWinners(matches) == [[1, 2, 10], [4, 5, 7, 8]]

    matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
    assert Solution().findWinners(matches) == [[1, 2, 5, 6], []]


if __name__ == '__main__':
    main()
