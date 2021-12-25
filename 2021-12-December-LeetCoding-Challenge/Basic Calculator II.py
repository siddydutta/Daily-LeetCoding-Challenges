# -*- coding: utf-8 -*-
class Solution:
    def calculate(self, s: str) -> int:
        ''' Straightforward stack based solution. '''
        s = s.replace(' ', '')  # Remove whitespaces
        num, stack, sign = int(), list(), '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num*10 + int(ch)
            if not ch.isdigit() or i == len(s)-1:
                # Evaluate if * or / or last ch in string
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign, num = ch, int()
        return sum(stack)


def main():
    s = "3+2*2"
    assert Solution().calculate(s) == 7

    s = " 3/2 "
    assert Solution().calculate(s) == 1

    s = " 3+5 / 2"
    assert Solution().calculate(s) == 5

    s = "14-3/2"
    assert Solution().calculate(s) == 13


if __name__ == '__main__':
    main()
