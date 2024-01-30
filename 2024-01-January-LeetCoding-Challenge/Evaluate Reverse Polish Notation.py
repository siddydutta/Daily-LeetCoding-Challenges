from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        while tokens:
            token = tokens.pop(0)
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                n2, n1 = stack.pop(), stack.pop()
                res = eval(f'{n1}{token}{n2}')
                stack.append(int(res))
        return stack[-1]


def main():
    tokens = ['2', '1', '+', '3', '*']
    assert Solution().evalRPN(tokens) == 9

    tokens = ['4', '13', '5', '/', '+']
    assert Solution().evalRPN(tokens) == 6

    tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
    assert Solution().evalRPN(tokens) == 22


if __name__ == '__main__':
    main()
