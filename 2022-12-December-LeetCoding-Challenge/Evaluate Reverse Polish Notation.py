# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                expr = f'{left}{token}{right}'
                stack.append(int(eval(expr)))
        return stack.pop()


def main():
    tokens = ["2", "1", "+", "3", "*"]
    assert Solution().evalRPN(tokens) == 9

    tokens = ["4", "13", "5", "/", "+"]
    assert Solution().evalRPN(tokens) == 6

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert Solution().evalRPN(tokens) == 22


if __name__ == '__main__':
    main()
