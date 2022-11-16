class Solution:
    def guessNumber(self, n: int, guess) -> int:
        first = 1
        last = n
        while first <= last:
            mid = (first + last) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                first = mid + 1
            elif res == -1:
                last = mid - 1
        return


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guessAPI(pick: int):
    return lambda t: 0 if t == pick else 1 if t < pick else -1


def main():
    n = 10
    pick = 6
    assert Solution().guessNumber(n, guessAPI(pick)) == pick

    n = 1
    pick = 1
    assert Solution().guessNumber(n, guessAPI(pick)) == pick

    n = 2
    pick = 1
    assert Solution().guessNumber(n, guessAPI(pick)) == pick


if __name__ == '__main__':
    main()
