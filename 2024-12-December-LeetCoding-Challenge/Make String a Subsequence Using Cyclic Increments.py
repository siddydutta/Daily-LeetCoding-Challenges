class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l1, l2 = len(str1), len(str2)
        p2 = 0
        for p1 in range(l1):
            if p2 < l2 and (ord(str2[p2]) - ord(str1[p1])) % 26 <= 1:
                p2 += 1
        return p2 == l2


def main():
    str1 = 'abc'
    str2 = 'ad'
    assert Solution().canMakeSubsequence(str1, str2) is True

    str1 = 'zc'
    str2 = 'ad'
    assert Solution().canMakeSubsequence(str1, str2) is True

    str1 = 'ab'
    str2 = 'd'
    assert Solution().canMakeSubsequence(str1, str2) is False


if __name__ == '__main__':
    main()
