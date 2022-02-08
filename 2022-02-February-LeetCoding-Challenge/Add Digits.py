# -*- coding: utf-8 -*-
class Solution1:
    def addDigits(self, num: int) -> int:
        ''' Straightforward iterative solution. '''
        digits = list(map(int, str(num)))
        while len(digits) != 1:
            s = sum(digits)
            digits = list(map(int, str(s)))
        return digits[0]


class Solution2:
    def addDigits(self, num: int) -> int:
        ''' Simple O(1) math based solution. '''
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9


def main():
    for obj in [Solution1(), Solution2()]:
        num = 38
        assert obj.addDigits(num) == 2

        num = 0
        assert obj.addDigits(num) == 0


if __name__ == '__main__':
    main()
