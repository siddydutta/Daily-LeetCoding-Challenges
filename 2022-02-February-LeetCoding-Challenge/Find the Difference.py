# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ''' Counter based solution. '''
        s_count, t_count = Counter(s), Counter(t)
        for ch, count in t_count.items():
            if count != s_count.get(ch, 0):
                return ch
        return


def main():
    s, t = "abcd", "abcde"
    assert Solution().findTheDifference(s, t) == "e"

    s, t = "", "y"
    assert Solution().findTheDifference(s, t) == "y"


if __name__ == '__main__':
    main()
