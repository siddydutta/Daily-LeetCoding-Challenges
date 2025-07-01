class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = word[0]
        count = 1
        for ch in word[1:]:
            if ch == prev:
                count += 1
            else:
                prev = ch
        return count


def main():
    word = 'abbcccc'
    assert Solution().possibleStringCount(word) == 5

    word = 'abcd'
    assert Solution().possibleStringCount(word) == 1

    word = 'aaaa'
    assert Solution().possibleStringCount(word) == 4


if __name__ == '__main__':
    main()
