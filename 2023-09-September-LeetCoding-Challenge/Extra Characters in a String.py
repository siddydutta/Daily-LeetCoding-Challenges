from functools import lru_cache
from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @lru_cache(50)
        def get_extra(idx: int) -> int:
            if idx >= len(s):
                return 0
            curr_str = ''
            min_extra = len(s)
            for i in range(idx, len(s)):
                curr_str += s[i]
                curr_extra = 0 if curr_str in dictionary else len(curr_str)
                next_extra = get_extra(i+1)
                total_extra = curr_extra + next_extra
                min_extra = min(min_extra, total_extra)
            return min_extra

        dictionary = set(dictionary)
        return get_extra(0)


def main():
    s = "leetscode"
    dictionary = ["leet", "code", "leetcode"]
    assert Solution().minExtraChar(s, dictionary) == 1

    s = "sayhelloworld"
    dictionary = ["hello", "world"]
    assert Solution().minExtraChar(s, dictionary) == 3


if __name__ == '__main__':
    main()
