from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        n = len(digits)
        result = []
        for i in range(n):
            for j in range(i, n):
                num = int(digits[i:j+1])
                if low <= num <= high:
                    result.append(num)
        return sorted(result)


def main():
    low, high = 100, 300
    assert Solution().sequentialDigits(low, high) == [123, 234]

    low, high = 1000, 13000
    assert Solution().sequentialDigits(low, high) == [1234, 2345, 3456, 4567,
                                                      5678, 6789, 12345]


if __name__ == '__main__':
    main()
