class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n else 0

        p1, p2, p3 = 0, 1, 1
        for _ in range(n-2):
            p1, p2, p3 = p2, p3, p1+p2+p3
        return p3


def main():
    n = 4
    assert Solution().tribonacci(n) == 4

    n = 25
    assert Solution().tribonacci(n) == 1389537


if __name__ == '__main__':
    main()
