class Solution:
    def countHomogenous(self, s: str) -> int:
        res, count = 0, 0
        curr = None
        mod = 10**9 + 7
        for ch in s:
            count = count+1 if ch == curr else 1
            curr = ch
            res = (res + count) % mod
        return res


def main():
    s = 'abbcccaa'
    assert Solution().countHomogenous(s) == 13

    s = 'xy'
    assert Solution().countHomogenous(s) == 2

    s = 'zzzzz'
    assert Solution().countHomogenous(s) == 15


if __name__ == '__main__':
    main()
