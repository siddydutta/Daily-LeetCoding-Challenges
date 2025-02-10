class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


def main():
    s = 'abc'
    assert Solution().clearDigits(s) == 'abc'

    s = 'cb34'
    assert Solution().clearDigits(s) == ''


if __name__ == '__main__':
    main()
