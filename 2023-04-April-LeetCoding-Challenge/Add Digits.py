# -*- coding: utf-8 -*-
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            s = 0
            while num:
                s += num % 10
                num //= 10
            num = s
        return num


def main():
    num = 38
    assert Solution().addDigits(num) == 2

    num = 0
    assert Solution().addDigits(num) == 0


if __name__ == '__main__':
    main()
