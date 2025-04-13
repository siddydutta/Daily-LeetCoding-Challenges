class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd, even = n // 2, (n+1) // 2
        mod = 10**9 + 7
        return (pow(5, even, mod) * pow(4, odd, mod)) % mod


def main():
    n = 1
    assert Solution().countGoodNumbers(n) == 5

    n = 4
    assert Solution().countGoodNumbers(n) == 400

    n = 50
    assert Solution().countGoodNumbers(n) == 564908303


if __name__ == '__main__':
    main()
