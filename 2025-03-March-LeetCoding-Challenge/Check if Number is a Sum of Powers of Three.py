class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True


def main():
    n = 12
    assert Solution().checkPowersOfThree(n) is True

    n = 91
    assert Solution().checkPowersOfThree(n) is True

    n = 21
    assert Solution().checkPowersOfThree(n) is False


if __name__ == '__main__':
    main()
