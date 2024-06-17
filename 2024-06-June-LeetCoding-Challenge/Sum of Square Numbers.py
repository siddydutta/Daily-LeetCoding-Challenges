from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))
        while a <= b:
            s = a*a + b*b
            if s < c:
                a += 1
            elif s > c:
                b -= 1
            else:
                return True
        return False


def main():
    c = 5
    assert Solution().judgeSquareSum(c) is True

    c = 3
    assert Solution().judgeSquareSum(c) is False


if __name__ == '__main__':
    main()
