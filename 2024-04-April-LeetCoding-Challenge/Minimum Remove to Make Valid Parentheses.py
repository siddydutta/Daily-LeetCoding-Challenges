class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, result = list(), [''] * len(s)
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)  # Keep track of open
            elif ch == ')':
                if stack:
                    result[idx] = ch  # Include close
                    result[stack.pop()] = '('  # Include corresponding open
            else:
                result[idx] = ch  # Include all other ch
        return ''.join(result)


def main():
    s = 'lee(t(c)o)de)'
    assert Solution().minRemoveToMakeValid(s) == 'lee(t(c)o)de'

    s = 'a)b(c)d'
    assert Solution().minRemoveToMakeValid(s) == 'ab(c)d'

    s = '))(('
    assert Solution().minRemoveToMakeValid(s) == ''


if __name__ == '__main__':
    main()
