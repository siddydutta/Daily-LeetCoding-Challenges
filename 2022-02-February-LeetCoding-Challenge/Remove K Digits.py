# -*- coding: utf-8 -*-
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ''' Solution based on monotonic stack. '''
        stack = list()
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()  # Pop numbers greater than digit
                k -= 1
            stack.append(digit)
        if k > 0:
            # If remaining k, remove last k digits
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"


def main():
    num = "1432219"
    k = 3
    assert Solution().removeKdigits(num, k) == "1219"

    num = "10200"
    k = 1
    assert Solution().removeKdigits(num, k) == "200"

    num = "10"
    k = 2
    assert Solution().removeKdigits(num, k) == "0"


if __name__ == '__main__':
    main()
