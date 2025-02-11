class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= len(part) and ''.join(stack[-len(part):]) == part:
                for _ in range(len(part)):
                    stack.pop()
        return ''.join(stack)


def main():
    s = 'daabcbaabcbc'
    part = 'abc'
    assert Solution().removeOccurrences(s, part) == 'dab'

    s = 'axxxxyyyyb'
    part = 'xy'
    assert Solution().removeOccurrences(s, part) == 'ab'


if __name__ == '__main__':
    main()
