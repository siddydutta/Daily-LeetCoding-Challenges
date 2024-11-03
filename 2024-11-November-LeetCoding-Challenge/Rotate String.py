class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False


def main():
    s = 'abcde'
    goal = 'cdeab'
    assert Solution().rotateString(s, goal) is True

    s = 'abcde'
    goal = 'abced'
    assert Solution().rotateString(s, goal) is False


if __name__ == '__main__':
    main()
