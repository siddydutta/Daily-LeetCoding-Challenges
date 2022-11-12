from bisect import insort


class MedianFinder:
    def __init__(self):
        self.nums = list()

    def addNum(self, num: int) -> None:
        insort(self.nums, num)

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        if len(self.nums) % 2 == 0:
            return (self.nums[mid-1]+self.nums[mid]) / 2
        else:
            return self.nums[mid]


def main():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2.0


if __name__ == '__main__':
    main()
