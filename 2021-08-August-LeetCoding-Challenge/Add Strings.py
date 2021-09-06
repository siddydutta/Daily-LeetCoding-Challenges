# -*- coding: utf-8 -*-
class NaiveSolution:
    '''
    Return the sum of num1 and num2.
    Cannot convert the inputs to integers directly.
    Pythonic solution.
    '''
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(num1 + "+" + num2))


class Solution:
    def __get_int(self, num: str) -> int:
        ''' Parses a string into integer. '''
        ORD_CONSTANT = 48
        return ord(num) - ORD_CONSTANT

    def addStrings(self, num1: str, num2: str) -> str:
        # Ensure num1 is the larger number (in terms of length)
        if len(num2) > len(num1):
            num1, num2 = num2, num1  # Swap

        res = str()
        common_length = len(num2)  # Since num2 will have lesser length
        carry = 0

        # Digit by digit addition maintaining carry
        for pos in range(1, common_length+1):
            digit_sum = self.__get_int(num1[-pos]) + self.__get_int(num2[-pos])
            digit_sum += carry  # Add carry
            carry = 0  # Reset carry
            if digit_sum >= 10:
                carry = 1  # Set carry
                digit_sum -= 10  # Keep remainder
            res = str(digit_sum) + res

        # For all extra digits in num1, repeat addition with carry
        for pos in range(1, len(num1) - common_length + 1):
            digit_sum = self.__get_int(num1[-(pos + common_length)]) + carry
            carry = 0
            if digit_sum >= 10:
                carry = 1
                digit_sum -= 10
            res = str(digit_sum) + res

        if carry:
            res = "1" + res  # Add remaining carry, if any
        return res


def main():
    num1 = "11"
    num2 = "123"
    assert Solution().addStrings(num1, num2) == "134"

    num1 = "0"
    num2 = "0"
    assert Solution().addStrings(num1, num2) == "0"

    num1 = "456"
    num2 = "78"
    assert Solution().addStrings(num1, num2) == "534"

    num1 = "9"
    num2 = "99"
    assert Solution().addStrings(num1, num2) == "108"

    num1 = "9999"
    num2 = "9999"
    assert Solution().addStrings(num1, num2) == "19998"


if __name__ == '__main__':
    main()
