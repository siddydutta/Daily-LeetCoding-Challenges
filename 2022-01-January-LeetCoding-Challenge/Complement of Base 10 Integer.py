# -*- coding: utf-8 -*-
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ''' Bit manipulation based solution. Time Complexity: O(logn) '''
        binary = bin(n)[2:]  # Get binary representation of n
        length = 2**len(binary) - 1  # Get number represented by 11.. length
        return n ^ length  # XOR between n and 11..111 will give complement


def main():
    n = 5
    assert Solution().bitwiseComplement(n) == 2

    n = 7
    assert Solution().bitwiseComplement(n) == 0

    n = 10
    assert Solution().bitwiseComplement(n) == 5


if __name__ == '__main__':
    main()
