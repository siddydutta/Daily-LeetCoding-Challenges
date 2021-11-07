# -*- coding: utf-8 -*-
class NotSolution:
    ''' Simple Pythonic solution. '''
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(num1 + "*" + num2))


class Solution:
    ''' Simulation based answer, storing results in array positions. '''
    def multiply(self, num1: str, num2: str) -> str:
        idx = [0] * (len(num1)+len(num2))  # Store final answer digit wise

        # Perform multiplication right to left
        for i, d1 in reversed(list(enumerate(num1))):
            for j, d2 in reversed(list(enumerate(num2))):
                idx[i+j+1] += int(d1) * int(d2)  # Actual product
                idx[i+j] += idx[i+j+1] // 10  # Add carry
                idx[i+j+1] %= 10  # Keep only remainder as carry is added

        prod = "".join(list(map(str, idx))).lstrip('0')
        return prod if prod else '0'  # Edge case


def main():
    num1 = "2"
    num2 = "3"
    assert Solution().multiply(num1, num2) == "6"

    num1 = "123"
    num2 = "456"
    assert Solution().multiply(num1, num2) == "56088"

    num1 = "0"
    num2 = "0"
    assert Solution().multiply(num1, num2) == "0"


if __name__ == '__main__':
    main()
