# -*- coding: utf-8 -*-
class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()
        for ch in s:
            stack.pop() if ch == '*' else stack.append(ch)
        return ''.join(stack)


def main():
    s = "leet**cod*e"
    assert Solution().removeStars(s) == "lecoe"

    s = "erase*****"
    assert Solution().removeStars(s) == ""


if __name__ == '__main__':
    main()
