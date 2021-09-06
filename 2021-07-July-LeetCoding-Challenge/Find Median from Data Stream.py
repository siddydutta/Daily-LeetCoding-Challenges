# -*- coding: utf-8 -*-
from bisect import insort_left
from heapq import heappush, heappushpop


class MedianFinder1:
    '''
    Using bisect (binary search)
    Time Complexity for addNum: O(log n)
    Time Complexity for findMedian: O(1)
    '''
    def __init__(self):
        self.numbers = list()  # List of numbers
        self.n = int()  # Count of numbers

    def addNum(self, num: int) -> None:
        insort_left(self.numbers, num)
        self.n += 1

    def findMedian(self) -> float:
        mid = self.n // 2
        if self.n % 2 == 0:
            return (self.numbers[mid-1] + self.numbers[mid]) / 2
        else:
            return float(self.numbers[mid])


class MedianFinder:
    '''
    Using two heaps.
    '''
    def __init__(self):
        self.max_heap = list()  # Smaller half of the list (inverted nums)
        self.min_heap = list()  # Larger half of the list

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            # Insert inverted number in smaller half
            # And move largest number of smaller half to larger half
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:
            # Insert number in larger half
            # And move smallest number larger half to smaller half
            heappush(self.max_heap, -heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return float(self.min_heap[0])


def main():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2.0

    medianFinder = MedianFinder()
    medianFinder.addNum(6)
    assert medianFinder.findMedian() == 6.0
    medianFinder.addNum(10)
    assert medianFinder.findMedian() == 8.0
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 6.0
    medianFinder.addNum(6)
    assert medianFinder.findMedian() == 6.0
    medianFinder.addNum(5)
    assert medianFinder.findMedian() == 6.0
    medianFinder.addNum(0)
    assert medianFinder.findMedian() == 5.5
    medianFinder.addNum(6)
    assert medianFinder.findMedian() == 6.0
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 5.5
    medianFinder.addNum(1)
    assert medianFinder.findMedian() == 5.0
    medianFinder.addNum(0)
    assert medianFinder.findMedian() == 4.0
    medianFinder.addNum(0)
    assert medianFinder.findMedian() == 3.0


if __name__ == '__main__':
    main()
