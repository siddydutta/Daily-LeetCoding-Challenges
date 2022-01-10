# -*- coding: utf-8 -*-
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ''' Lazy solution, but accepted. '''
        return bin(int(a, 2) + int(b, 2))[2:]


def main():
    a = "11"
    b = "1"
    assert Solution().addBinary(a, b) == "100"

    a = "1010"
    b = "1011"
    assert Solution().addBinary(a, b) == "10101"


if __name__ == '__main__':
    main()
