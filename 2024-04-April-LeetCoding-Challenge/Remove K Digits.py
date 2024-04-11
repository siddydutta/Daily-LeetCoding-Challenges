class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = list()
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                # monotonic stack logic
                k -= 1
                stack.pop()
            stack.append(digit)
        if k:
            # exclude the largest digits
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'


def main():
    num = '1432219'
    k = 3
    assert Solution().removeKdigits(num, k) == '1219'

    num = '10200'
    k = 1
    assert Solution().removeKdigits(num, k) == '200'

    num = '10'
    k = 2
    assert Solution().removeKdigits(num, k) == '0'


if __name__ == '__main__':
    main()
