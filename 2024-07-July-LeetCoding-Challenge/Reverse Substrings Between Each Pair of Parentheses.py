class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        for ch in s:
            if ch == ')':
                temp = ''
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(ch)
        return ''.join(stack)


def main():
    s = '(abcd)'
    assert Solution().reverseParentheses(s) == 'dcba'

    s = '(u(love)i)'
    assert Solution().reverseParentheses(s) == 'iloveu'

    s = '(ed(et(oc))el)'
    assert Solution().reverseParentheses(s) == 'leetcode'


if __name__ == '__main__':
    main()
