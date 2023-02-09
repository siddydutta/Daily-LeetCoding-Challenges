# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for _ in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - 97].add(idea[1:])

        count = 0
        for i in range(25):
            for j in range(i+1, 26):
                n = len(groups[i] & groups[j])
                count += 2 * (len(groups[i])-n) * (len(groups[j])-n)
        return count


def main():
    ideas = ["coffee", "donuts", "time", "toffee"]
    assert Solution().distinctNames(ideas) == 6

    ideas = ["lack", "back"]
    assert Solution().distinctNames(ideas) == 0


if __name__ == '__main__':
    main()
