class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i-1]) - ord(s[i]))
        return score


def main():
    s = 'hello'
    assert Solution().scoreOfString(s) == 13

    s = 'zaz'
    assert Solution().scoreOfString(s) == 50


if __name__ == '__main__':
    main()
