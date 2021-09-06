# -*- coding: utf-8 -*-
import math


class Solution:
    ''' Straight forward solution'''
    def __is_square(self, num: int) -> bool:
        sqrt = int(math.sqrt(num))
        return sqrt*sqrt == num

    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)+1)):
            # If 0 <= a <= sqrt(c)
            b = c - a*a  # As a^2 + b^2 = c
            if self.__is_square(b):
                # Check if b^2 is valid
                #print(a, b)
                return True
        return False


def main():
    c = 5
    assert Solution().judgeSquareSum(c)

    c = 3
    assert not Solution().judgeSquareSum(c)

    c = 4
    assert Solution().judgeSquareSum(c)

    c = 2
    assert Solution().judgeSquareSum(c)

    c = 1
    assert Solution().judgeSquareSum(c)


if __name__ == '__main__':
    main()
