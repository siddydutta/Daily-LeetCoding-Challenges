# -*- coding: utf-8 -*-
class Solution:
    ''' Simple pythonic XOR based solution. '''
    def hammingDistance(self, x: int, y: int) -> int:
        xor = bin(x ^ y)
        return xor.count('1')


def main():
    x, y = 1, 4
    assert Solution().hammingDistance(x, y) == 2

    x, y = 3, 1
    assert Solution().hammingDistance(x, y) == 1

    x, y = 0, 2147483647
    assert Solution().hammingDistance(x, y) == 31


if __name__ == '__main__':
    main()
