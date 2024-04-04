class Solution:
    def maxDepth(self, s: str) -> int:
        count, max_count = 0, 0
        for ch in s:
            if ch == '(':
                count += 1
                max_count = max(max_count, count)
            elif ch == ')':
                count -= 1
        return max_count


def main():
    s = '(1+(2*3)+((8)/4))+1'
    assert Solution().maxDepth(s) == 3

    s = '(1)+((2))+(((3)))'
    assert Solution().maxDepth(s) == 3

    s = '()'
    assert Solution().maxDepth(s) == 1

    s = '+(+(+)+)+'
    assert Solution().maxDepth(s) == 2

    s = '(1())'
    assert Solution().maxDepth(s) == 2


if __name__ == '__main__':
    main()
