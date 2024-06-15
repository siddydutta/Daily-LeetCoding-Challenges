from heapq import heappop, heappush
from typing import List


class Project:
    def __init__(self, capital: int, profit: int):
        self.capital = capital
        self.profit = profit


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = [Project(capital=c, profit=p)
                    for c, p in zip(capital, profits)]
        projects.sort(key=lambda p: p.capital, reverse=True)

        max_heap = []
        for _ in range(k):
            while projects and projects[-1].capital <= w:
                # add all possible projects to max_heap
                heappush(max_heap, -projects.pop().profit)
            if max_heap:
                # add max profit to remaining capital
                w += -heappop(max_heap)
            else:
                # no projects possible
                break

        return w


def main():
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    assert Solution().findMaximizedCapital(k, w, profits, capital) == 4

    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    assert Solution().findMaximizedCapital(k, w, profits, capital) == 6


if __name__ == "__main__":
    main()
