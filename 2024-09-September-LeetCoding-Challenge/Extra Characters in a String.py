from functools import lru_cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)

        @lru_cache(None)
        def get_extra(idx: int = 0) -> int:
            if idx == n:
                return 0
            curr_str = ''
            min_extra = n
            for i in range(idx, n):
                curr_str += s[i]
                curr_extra = 0 if curr_str in dictionary else len(curr_str)
                next_extra = get_extra(i+1)
                min_extra = min(min_extra, curr_extra+next_extra)
            return min_extra

        return get_extra()


def main():
    s = 'leetscode'
    dictionary = ['leet', 'code', 'leetcode']
    assert Solution().minExtraChar(s, dictionary) == 1

    s = 'sayhelloworld'
    dictionary = ['hello', 'world']
    assert Solution().minExtraChar(s, dictionary) == 3


if __name__ == '__main__':
    main()
