# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ''' Naive solution. '''
        return list(map(int, str(int(''.join(map(str, num))) + k)))


def main():
    num, k = [1, 2, 0, 0], 34
    assert Solution().addToArrayForm(num, k) == [1, 2, 3, 4]

    num, k = [2, 7, 4], 181
    assert Solution().addToArrayForm(num, k) == [4, 5, 5]

    num, k = [2, 1, 5], 806
    assert Solution().addToArrayForm(num, k) == [1, 0, 2, 1]


if __name__ == '__main__':
    main()
