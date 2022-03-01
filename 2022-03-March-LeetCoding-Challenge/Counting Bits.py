# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ''' Dynamic programming based solution. '''
        counter = [0]
        for i in range(1, n+1):
            # counter.append(counter[i // 2] + (i % 2))
            counter.append(counter[i >> 1] + (i & 1))
        return counter


def main():
    n = 2
    assert Solution().countBits(n) == [0, 1, 1]

    n = 5
    assert Solution().countBits(n) == [0, 1, 1, 2, 1, 2]


if __name__ == '__main__':
    main()
