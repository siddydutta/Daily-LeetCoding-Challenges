# -*- coding: utf-8 -*-
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()

        for ch in s:
            stack.append(ch)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

        return ''.join(stack)


def main():
    obj = Solution()

    s = "abbaca"
    assert obj.removeDuplicates(s) == "ca"

    s = "azxxzy"
    assert obj.removeDuplicates(s) == "ay"


if __name__ == '__main__':
    main()
