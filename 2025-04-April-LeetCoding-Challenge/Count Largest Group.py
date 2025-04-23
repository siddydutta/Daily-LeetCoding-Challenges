class Solution:
    def __digit_sum(self, num: int) -> int:
        s = 0
        while num != 0:
            s += num % 10
            num //= 10
        return s

    def countLargestGroup(self, n: int) -> int:
        counts = [0] * 37
        max_count = 0
        for num in range(1, n + 1):
            group = self.__digit_sum(num)
            counts[group] += 1
            max_count = max(max_count, counts[group])
        return sum([count == max_count for count in counts])


def main():
    n = 13
    assert Solution().countLargestGroup(n) == 4

    n = 2
    assert Solution().countLargestGroup(n) == 2


if __name__ == '__main__':
    main()
