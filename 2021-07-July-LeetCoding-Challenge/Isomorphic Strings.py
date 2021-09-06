# -*- coding: utf-8 -*-
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chMap = dict()
        alreadyMapped = set()

        for i in range(len(s)):
            if s[i] in chMap:
                if chMap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in alreadyMapped:
                    return False
                else:
                    chMap[s[i]] = t[i]
                    alreadyMapped.add(t[i])

        return True


def main():
    obj = Solution()

    s = "egg"
    t = "add"
    assert obj.isIsomorphic(s, t)

    s = "foo"
    t = "bar"
    assert not obj.isIsomorphic(s, t)

    s = "paper"
    t = "title"
    assert obj.isIsomorphic(s, t)


if __name__ == '__main__':
    main()
