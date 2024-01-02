from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        res = []
        while True:
            temp = []
            for key, value in freq.items():
                if value != 0:
                    temp.append(key)
                    freq[key] -= 1
            if not temp:
                break
            res.append(temp)
        return res


def main():
    nums = [1, 3, 4, 1, 2, 3, 1]
    assert Solution().findMatrix(nums) == [[1, 3, 4, 2], [1, 3], [1]]

    nums = [1, 2, 3, 4]
    assert Solution().findMatrix(nums) == [[1, 2, 3, 4]]


if __name__ == '__main__':
    main()
