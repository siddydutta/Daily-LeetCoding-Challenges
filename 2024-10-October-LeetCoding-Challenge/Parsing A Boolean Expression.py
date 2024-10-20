class Solution:
    BOOL_MAP = {'t': True, 'f': False}

    def parseBoolExpr(self, expression: str) -> bool:
        stack = list()
        for ch in expression:
            if ch == ')':
                vals = set()
                while stack[-1] != '(':
                    vals.add(stack.pop())
                stack.pop()
                operation = stack.pop()
                if operation == '&':
                    stack.append(all(vals))
                elif operation == '|':
                    stack.append(any(vals))
                else:
                    stack.append(not vals.pop())
            elif ch != ',':
                stack.append(self.BOOL_MAP.get(ch, ch))
        return stack.pop()


def main():
    expression = '&(|(f))'
    assert Solution().parseBoolExpr(expression) is False

    expression = '|(f,f,f,t)'
    assert Solution().parseBoolExpr(expression) is True

    expression = '!(&(f,t))'
    assert Solution().parseBoolExpr(expression) is True


if __name__ == '__main__':
    main()
