class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == 'B' and stack and stack[-1] == 'A':
                stack.pop()
            elif ch == 'D' and stack and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)


def main():
    s = 'ABFCACDB'
    assert Solution().minLength(s) == 2

    s = 'ACBBD'
    assert Solution().minLength(s) == 5


if __name__ == '__main__':
    main()
