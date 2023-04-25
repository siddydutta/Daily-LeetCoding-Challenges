# -*- coding: utf-8 -*-
from heapq import heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.min_heap = list()

    def popSmallest(self) -> int:
        if self.min_heap:
            return heappop(self.min_heap)
        self.current += 1
        return self.current - 1

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.min_heap:
            heappush(self.min_heap, num)


def main():
    smallest_infinite_set = SmallestInfiniteSet()
    assert smallest_infinite_set.popSmallest() == 1
    assert smallest_infinite_set.popSmallest() == 2
    assert smallest_infinite_set.popSmallest() == 3
    smallest_infinite_set.addBack(2)
    assert smallest_infinite_set.popSmallest() == 2
    assert smallest_infinite_set.popSmallest() == 4
    smallest_infinite_set.addBack(1)
    smallest_infinite_set.addBack(2)
    smallest_infinite_set.addBack(3)
    assert smallest_infinite_set.popSmallest() == 1
    assert smallest_infinite_set.popSmallest() == 2
    assert smallest_infinite_set.popSmallest() == 3
    assert smallest_infinite_set.popSmallest() == 5


if __name__ == '__main__':
    main()
