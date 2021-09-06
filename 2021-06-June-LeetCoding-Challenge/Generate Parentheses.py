# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = list()

        def generate(string, pos, start, stop):
            if stop == n:
                parentheses.append(''.join(string))
                return
            if start > stop:
                string[pos] = ")"
                generate(string, pos+1, start, stop+1)
            if start < n:
                string[pos] = "("
                generate(string, pos+1, start+1, stop)

        generate([""] * 2 * n, 0, 0, 0)
        return parentheses


if __name__ == '__main__':
    obj = Solution()
    n = 1
    assert obj.generateParenthesis(n) == ["()"]

    n = 3
    assert set(obj.generateParenthesis(n)) == set(["((()))", "(()())",
                                                   "(())()", "()(())",
                                                   "()()()"])
