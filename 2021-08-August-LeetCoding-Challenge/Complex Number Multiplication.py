# -*- coding: utf-8 -*-
class Solution:
    ''' Using the formula: (a+bi)(c+di) = (ac−bd) + (ad+bc)i '''
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))
        real = a*c - b*d
        imag = a*d + b*c
        return f"{real}+{imag}i"


def main():
    num1 = "1+1i"
    num2 = "1+1i"
    assert Solution().complexNumberMultiply(num1, num2) == "0+2i"

    num1 = "1+-1i"
    num2 = "1+-1i"
    assert Solution().complexNumberMultiply(num1, num2) == "0+-2i"


if __name__ == '__main__':
    main()
