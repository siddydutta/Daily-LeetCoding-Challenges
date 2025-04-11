class Solution:
    def __is_symmetric(self, num: int) -> bool:
        if num < 10:
            return False
        if num < 100:
            d1 = num % 10
            d2 = num // 10
            return d1 == d2
        if num < 1_000:
            return False
        if num < 10_000:
            d1 = num % 10
            num //= 10
            d2 = num % 10
            num //= 10
            d3 = num % 10
            num //= 10
            d4 = num % 10
            return d1 + d2 == d3 + d4
        return False

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(map(self.__is_symmetric, range(low, high+1)))


def main():
    low = 1
    high = 100
    assert Solution().countSymmetricIntegers(low, high) == 9

    low = 1200
    high = 1230
    assert Solution().countSymmetricIntegers(low, high) == 4


if __name__ == '__main__':
    main()
