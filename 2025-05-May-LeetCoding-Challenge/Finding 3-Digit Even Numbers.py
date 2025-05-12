from collections import Counter


class Solution:
    def __is_number(self, num: int) -> bool:
        freqs = Counter(str(num))
        return freqs == (self.counts & freqs)

    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        self.counts = Counter(map(str, digits))
        return list(filter(self.__is_number, range(100, 1000, 2)))


def main():
    digits = [2, 1, 3, 0]
    assert Solution().findEvenNumbers(digits) == [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]

    digits = [2, 2, 8, 8, 2]
    assert Solution().findEvenNumbers(digits) == [222, 228, 282, 288, 822, 828, 882]

    digits = [3, 7, 5]
    assert Solution().findEvenNumbers(digits) == []


if __name__ == '__main__':
    main()
