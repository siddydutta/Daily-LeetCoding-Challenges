from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counts2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counts2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        result = 0
        for n1 in self.nums1:
            result += self.counts2[tot - n1]
        return result


def main():
    obj = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
    assert obj.count(7) == 8
    obj.add(3, 2)
    assert obj.count(8) == 2
    assert obj.count(4) == 1
    obj.add(0, 1)
    obj.add(1, 1)
    assert obj.count(7) == 11


if __name__ == '__main__':
    main()
