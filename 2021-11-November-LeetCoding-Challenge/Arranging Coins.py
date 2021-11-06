# -*- coding: utf-8 -*-
from math import sqrt


class Solution1:
    ''' Mathemtical solution: (-1 + √(1+8n))÷2 '''
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + sqrt(1+8*n)) // 2)


class Solution2:
    ''' Brute force solution. '''
    def arrangeCoins(self, n: int) -> int:
        row = 1
        while n-row >= 0:
            n -= row
            row += 1
        return row-1


def main():
    for obj in [Solution1(), Solution2()]:
        n = 1
        assert obj.arrangeCoins(n) == 1

        n = 5
        assert obj.arrangeCoins(n) == 2

        n = 8
        assert obj.arrangeCoins(n) == 3

        n = 2**31-1
        assert obj.arrangeCoins(n) == 65535


if __name__ == '__main__':
    main()
