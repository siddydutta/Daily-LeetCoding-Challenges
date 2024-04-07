class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        for ch in s:
            if ch == '(' or ch == '*':
                count += 1
            else:
                count -= 1
                if count < 0:
                    # no ( for a )
                    return False
        if count == 0:
            # all ( have a )
            return True

        count = 0
        for ch in reversed(s):
            if ch == ')' or ch == '*':
                count += 1
            else:
                count -= 1
                if count < 0:
                    # no ) for a (
                    return False
        return True


def main():
    s = '()'
    assert Solution().checkValidString(s)

    s = '(*)'
    assert Solution().checkValidString(s)

    s = '(*))'
    assert Solution().checkValidString(s)


if __name__ == '__main__':
    main()
