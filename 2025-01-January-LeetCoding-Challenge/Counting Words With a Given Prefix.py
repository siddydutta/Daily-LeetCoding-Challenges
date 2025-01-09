from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([word.startswith(pref) for word in words])


def main():
    words = ['pay', 'attention', 'practice', 'attend']
    pref = 'at'
    assert Solution().prefixCount(words, pref) == 2

    words = ['leetcode', 'win', 'loops', 'success']
    pref = 'code'
    assert Solution().prefixCount(words, pref) == 0


if __name__ == '__main__':
    main()
