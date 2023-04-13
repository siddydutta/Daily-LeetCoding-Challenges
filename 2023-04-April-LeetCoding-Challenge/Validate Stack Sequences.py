# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ptr, stack = 0, list()
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[ptr]:
                stack.pop()
                ptr += 1
        return not stack


def main():
    pushed, popped = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
    assert Solution().validateStackSequences(pushed, popped)

    pushed, popped = [1, 2, 3, 4, 5], [4, 3, 5, 1, 2]
    assert not Solution().validateStackSequences(pushed, popped)


if __name__ == '__main__':
    main()
