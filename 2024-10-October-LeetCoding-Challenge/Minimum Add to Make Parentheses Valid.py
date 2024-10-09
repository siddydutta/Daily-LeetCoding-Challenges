class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n_open, n_close = 0, 0
        for ch in s:
            if ch == '(':
                n_open += 1
            elif n_open > 0:
                n_open -= 1
            else:
                n_close += 1
        return n_open + n_close


def main():
    s = '())'
    assert Solution().minAddToMakeValid(s) == 1

    s = '((('
    assert Solution().minAddToMakeValid(s) == 3


if __name__ == '__main__':
    main()
