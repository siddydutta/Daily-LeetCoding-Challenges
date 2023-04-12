# -*- coding: utf-8 -*-
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)


def main():
    path = "/home/"
    assert Solution().simplifyPath(path) == "/home"

    path = "/../"
    assert Solution().simplifyPath(path) == "/"

    path = "/home//foo/"
    assert Solution().simplifyPath(path) == "/home/foo"


if __name__ == '__main__':
    main()
