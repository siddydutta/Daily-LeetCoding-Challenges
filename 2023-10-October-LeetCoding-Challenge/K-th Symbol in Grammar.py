class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2 == 0:
            return 1 if self.kthGrammar(n-1, k//2) == 0 else 0
        else:
            return 0 if self.kthGrammar(n-1, (k+1)//2) == 0 else 1


def main():
    n, k = 1, 1
    assert Solution().kthGrammar(n, k) == 0

    n, k = 2, 1
    assert Solution().kthGrammar(n, k) == 0

    n, k = 2, 2
    assert Solution().kthGrammar(n, k) == 1


if __name__ == '__main__':
    main()
