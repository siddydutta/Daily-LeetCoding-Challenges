from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_freq = Counter(chars)
        lengths = 0
        for word in words:
            word_freq = Counter(word)
            can_form = True
            for key, value in word_freq.items():
                if value > chars_freq[key]:
                    can_form = False
                    break
            if can_form:
                lengths += len(word)
        return lengths


def main():
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    assert Solution().countCharacters(words, chars) == 6

    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    assert Solution().countCharacters(words, chars) == 10


if __name__ == '__main__':
    main()
