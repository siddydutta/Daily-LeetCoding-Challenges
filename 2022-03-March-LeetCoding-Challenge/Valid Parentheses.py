# -*- coding: utf-8 -*-
class Solution:
    def isValid(self, s: str) -> bool:
        ''' Stack based solution. '''
        brackets = {')': '(', '}': '{', ']': '['}
        stack = list()

        for bracket in s:
            # Open bracket condition
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if stack and stack[-1] == brackets.get(bracket, None):
                    stack.pop()
                else:
                    return False

        # Every bracket should be closed
        if not stack:
            return True
        return False


def main():
    s = "()"
    assert Solution().isValid(s)

    s = "()[]{}"
    assert Solution().isValid(s)

    s = "(]"
    assert not Solution().isValid(s)


if __name__ == '__main__':
    main()
