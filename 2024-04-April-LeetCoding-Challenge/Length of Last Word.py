class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        for idx, ch in enumerate(reversed(s)):
            if ch == ' ':
                return idx
        return idx+1


def main():
    s = 'Hello World'
    assert Solution().lengthOfLastWord(s) == 5

    s = '   fly me   to   the moon  '
    assert Solution().lengthOfLastWord(s) == 4

    s = 'luffy is still joyboy'
    assert Solution().lengthOfLastWord(s) == 6

    s = 'a'
    assert Solution().lengthOfLastWord(s) == 1


if __name__ == '__main__':
    main()
