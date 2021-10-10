# -*- coding: utf-8 -*-
class Solution:
    ''' Brian Kernighan's algorithm. '''
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= (right-1)
        return right


def main():
    left = 5
    right = 7
    assert Solution().rangeBitwiseAnd(left, right) == 4

    left = 0
    right = 0
    assert Solution().rangeBitwiseAnd(left, right) == 0

    left = 1
    right = 2147483647
    assert Solution().rangeBitwiseAnd(left, right) == 0


if __name__ == '__main__':
    main()
