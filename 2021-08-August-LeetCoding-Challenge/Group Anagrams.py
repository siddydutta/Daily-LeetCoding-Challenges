# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # Sorted string -> Anagrams

        for s in strs:
            # Anagrams are made of the same sorted string
            sorted_str = "".join(sorted(s))
            groups[sorted_str].append(s)

        return groups.values()


def main():
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    ans = Solution().groupAnagrams(strs)
    assert ['bat'] in ans
    assert ['tan', 'nat'] in ans
    assert ['eat', 'tea', 'ate'] in ans


if __name__ == '__main__':
    main()
