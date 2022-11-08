class Solution:
    def makeGood(self, s: str) -> str:
        stack = list()
        for i in range(len(s)):
            # check if last ch on stack is toggle case of s[i]
            if stack and abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)


def main():
    s = "leEeetcode"
    assert Solution().makeGood(s) == "leetcode"

    s = "abBAcC"
    assert Solution().makeGood(s) == ""

    s = "s"
    assert Solution().makeGood(s) == "s"


if __name__ == '__main__':
    main()
