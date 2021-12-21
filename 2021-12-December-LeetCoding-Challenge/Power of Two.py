# -*- coding: utf-8 -*-
class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        ''' Bit count based solution. '''
        return n > 0 and bin(n).count('1') == 1


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        ''' Iterative solution. '''
        if n < 0:
            return False

        while n % 2 == 0:
            n /= 2
        return n == 1


def main():
    for obj in [Solution1(), Solution2()]:
        n = 1
        assert obj.isPowerOfTwo(n)

        n = 16
        assert obj.isPowerOfTwo(n)

        n = 3
        assert not obj.isPowerOfTwo(n)

        n = 1073741824
        assert obj.isPowerOfTwo(n)

        n = 2**31 - 1
        assert not obj.isPowerOfTwo(n)


if __name__ == '__main__':
    main()
