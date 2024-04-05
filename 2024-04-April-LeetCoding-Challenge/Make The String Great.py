class Solution:
    DIFF = ord('a') - ord('A')

    def makeGood(self, s: str) -> str:
        stack = list()
        for ch in s:
            if stack and abs(ord(ch) - ord(stack[-1])) == self.DIFF:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


def main():
    s = 'leEeetcode'
    assert Solution().makeGood(s) == 'leetcode'

    s = 'abBAcC'
    assert Solution().makeGood(s) == ''

    s = 's'
    assert Solution().makeGood(s) == 's'


if __name__ == '__main__':
    main()
