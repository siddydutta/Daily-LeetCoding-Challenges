# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:
        INV_MAP = {')': '(', ']': '[', '}': '{'}
        stack = list()
        for ch in s:
            if ch in INV_MAP:
                # check if closing bracket is in correct order
                if not stack or stack.pop() != INV_MAP[ch]:
                    return False
            else:
                stack.append(ch)
        # check if all brackets are closed
        return not stack


def main():
    s = "()"
    assert Solution().isValid(s)

    s = "()[]{}"
    assert Solution().isValid(s)

    s = "(]"
    assert not Solution().isValid(s)


if __name__ == '__main__':
    main()
