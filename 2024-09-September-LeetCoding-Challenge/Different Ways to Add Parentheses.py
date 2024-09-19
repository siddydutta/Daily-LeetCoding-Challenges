from typing import List


class Solution:
    def __init__(self):
        self.OPERATION = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }
        self.memo = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]

        result = []
        for i, ch in enumerate(expression):
            if ch in self.OPERATION:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for n1 in left:
                    for n2 in right:
                        result.append(self.OPERATION[ch](n1, n2))
        if not result:
            # no ops, expression is a number
            result.append(int(expression))

        self.memo[expression] = result
        return result


def main():
    expression = '2-1-1'
    assert Solution().diffWaysToCompute(expression) == [2, 0]

    expression = '2*3-4*5'
    assert Solution().diffWaysToCompute(expression) == [-34, -10, -14, -10, 10]


if __name__ == '__main__':
    main()
