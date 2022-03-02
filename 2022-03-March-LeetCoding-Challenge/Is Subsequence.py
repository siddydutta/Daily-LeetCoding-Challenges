# -*- coding: utf-8 -*-
class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        ''' Brute force solution. '''
        index = 0
        for ch in s:
            index = t.find(ch, index) + 1
            if not index:
                return False
        return True


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        ''' Straightforward solution. '''
        if s == "":
            return True

        index = 0
        for ch in t:
            if index < len(s):
                if ch == s[index]:
                    index += 1

        if index == len(s):
            return True
        return False


def main():
    for obj in [Solution1(), Solution2()]:
        s, t = "abc", "ahbgdc"
        assert obj.isSubsequence(s, t)

        s, t = "axc", "ahbgdc"
        assert not obj.isSubsequence(s, t)


if __name__ == '__main__':
    main()
