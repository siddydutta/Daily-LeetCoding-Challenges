# -*- coding: utf-8 -*-
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ''' Naive solution. '''
        return bin(int(a, 2) + int(b, 2))[2:]


def main():
    a, b = '11', '1'
    assert Solution().addBinary(a, b) == '100'

    a, b = '1010', '1011'
    assert Solution().addBinary(a, b) == '10101'


if __name__ == '__main__':
    main()
