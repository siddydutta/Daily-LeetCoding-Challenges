class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


def main():
    s = "abbaca"
    assert Solution().removeDuplicates(s) == "ca"

    s = "azxxzy"
    assert Solution().removeDuplicates(s) == "ay"


if __name__ == '__main__':
    main()
