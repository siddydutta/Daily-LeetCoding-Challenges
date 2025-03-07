class Solution:
    def __sieve(self, upper_limit: int) -> list[int]:
        sieve = [True] * (upper_limit+1)
        sieve[0] = sieve[1] = False
        for num in range(2, int(upper_limit**0.5)+1):
            if sieve[num]:
                for multiple in range(num*num, upper_limit+1, num):
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = self.__sieve(right)
        prime_numbers = [num for num in range(left, right+1) if sieve[num]]

        pair = [-1, -1]
        min_diff = float('inf')
        if len(prime_numbers) < 2:
            return pair

        for idx in range(1, len(prime_numbers)):
            diff = prime_numbers[idx] - prime_numbers[idx-1]
            if diff < min_diff:
                min_diff = diff
                pair = [prime_numbers[idx-1], prime_numbers[idx]]
        return pair


def main():
    left, right = 10, 19
    assert Solution().closestPrimes(left, right) == [11, 13]

    left, right = 4, 6
    assert Solution().closestPrimes(left, right) == [-1, -1]


if __name__ == '__main__':
    main()
