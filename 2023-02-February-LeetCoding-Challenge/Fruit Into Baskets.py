# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_types = Counter()
        distinct, max_fruits = 0, 0

        left, right = 0, 0
        while right < len(fruits):
            if fruit_types[fruits[right]] == 0:
                distinct += 1
            fruit_types[fruits[right]] += 1

            while distinct > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    distinct -= 1
                left += 1

            max_fruits = max(max_fruits, right-left+1)
            right += 1

        return max_fruits


def main():
    fruits = [1, 2, 1]
    assert Solution().totalFruit(fruits) == 3

    fruits = [0, 1, 2, 2]
    assert Solution().totalFruit(fruits) == 3

    fruits = [1, 2, 3, 2, 2]
    assert Solution().totalFruit(fruits) == 4


if __name__ == '__main__':
    main()
