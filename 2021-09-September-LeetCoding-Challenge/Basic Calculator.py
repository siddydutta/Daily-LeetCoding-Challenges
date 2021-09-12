# -*- coding: utf-8 -*-
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        sign = 1  # 1 indicates +, -1 indicates -1
        stack = list()
        operand = 0  # Number before operator

        for ch in s:
            if ch.isdigit():
                # Add digit as previous number
                operand = (operand*10) + int(ch)
            elif ch == '+':
                result += sign * operand  # Compute result
                operand = 0  # Reset previous number
                sign = 1  # Set sign for next operand as +
            elif ch == '-':
                result += sign * operand  # Compute result
                operand = 0  # Reset previous number
                sign = -1  # Set sign for next operand as -
            elif ch == '(':
                stack.append(result)  # First append previous computed result
                stack.append(sign)  # Second append previous sign
                operand = 0  # Reset previous number
                result = 0  # Reset result
                sign = 1
            elif ch == ')':
                result += sign * operand  # Compute result
                result *= stack.pop()  # First pop sign
                result += stack.pop()  # Second pop previous result
                operand = 0
                sign = 1

        result += sign * operand
        return result


def main():
    s = "1 + 1"
    assert Solution().calculate(s) == 2

    s = " 2-1 + 2 "
    assert Solution().calculate(s) == 3

    s = "(1+(4+5+2)-3)+(6+8)"
    assert Solution().calculate(s) == 23


if __name__ == '__main__':
    main()
