class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for ch in s:
            if ch == t[i]:
                i += 1
                if i == len(t):
                    # t is a subsequence of s
                    return 0
        # return remaining chars in t
        return len(t) - i


def main():
    s = 'coaching'
    t = 'coding'
    assert Solution().appendCharacters(s, t) == 4

    s = 'abcde'
    t = 'a'
    assert Solution().appendCharacters(s, t) == 0

    s = 'z'
    t = 'abcde'
    assert Solution().appendCharacters(s, t) == 5


if __name__ == '__main__':
    main()
