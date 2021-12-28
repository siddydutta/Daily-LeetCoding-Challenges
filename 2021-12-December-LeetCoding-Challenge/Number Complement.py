# -*- coding: utf-8 -*-
class Solution1:
    def findComplement(self, num: int) -> int:
        ''' Straightforwad solution. '''
        binary_num, complement = bin(num)[2:], str()
        for bit in binary_num:
            complement = complement + "0" if bit == "1" else complement + "1"
        return int(complement, 2)


class Solution2:
    def findComplement(self, num: int) -> int:
        ''' Bit manipulation based solution. '''
        return num ^ (2**num.bit_length() - 1)


def main():
    for obj in [Solution1(), Solution2()]:
        num = 5
        assert obj.findComplement(num) == 2

        num = 1
        assert obj.findComplement(num) == 0


if __name__ == '__main__':
    main()
