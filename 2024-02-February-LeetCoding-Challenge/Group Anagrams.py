from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            groups[sorted_str].append(s)
        return list(groups.values())


def main():
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    assert Solution().groupAnagrams(strs) == [['eat', 'tea', 'ate'],
                                              ['tan', 'nat'],
                                              ['bat']]

    strs = ['']
    assert Solution().groupAnagrams(strs) == [['']]

    strs = ['a']
    assert Solution().groupAnagrams(strs) == [['a']]


if __name__ == '__main__':
    main()
