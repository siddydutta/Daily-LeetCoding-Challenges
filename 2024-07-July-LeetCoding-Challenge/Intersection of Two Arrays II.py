from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        intersection = list()
        for key in counter1.keys():
            common = min(counter1.get(key), counter2.get(key, 0))
            intersection.extend([key] * common)
        return intersection


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert Solution().intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert Solution().intersect(nums1, nums2) == [4, 9]


if __name__ == '__main__':
    main()
