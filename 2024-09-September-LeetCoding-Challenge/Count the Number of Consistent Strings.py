from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        return len(words) - count


def main():
    allowed = 'ab'
    words = ['ad', 'bd', 'aaab', 'baa', 'badab']
    assert Solution().countConsistentStrings(allowed, words) == 2

    allowed = 'abc'
    words = ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
    assert Solution().countConsistentStrings(allowed, words) == 7

    allowed = 'cad'
    words = ['cc', 'acd', 'b', 'ba', 'bac', 'bad', 'ac', 'd']
    assert Solution().countConsistentStrings(allowed, words) == 4


if __name__ == '__main__':
    main()
