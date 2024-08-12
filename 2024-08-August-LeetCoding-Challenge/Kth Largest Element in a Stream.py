from heapq import heappush, heappushpop
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = list()
        for num in nums:
            self.__add_to_heap(num)

    def __add_to_heap(self, num: int) -> None:
        # keep track of self.k largest elements
        if len(self.heap) == self.k:
            if num > self.heap[0]:
                heappushpop(self.heap, num)
        else:
            heappush(self.heap, num)

    def add(self, val: int) -> int:
        self.__add_to_heap(val)
        # kth largest is the smallest in heap
        return self.heap[0]


def main():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8


if __name__ == '__main__':
    main()
