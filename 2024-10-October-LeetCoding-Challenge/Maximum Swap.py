class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(map(int, str(num)))
        max_idx = len(digits)-1
        x, y, = 0, 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[i] < digits[max_idx]:
                x, y = i, max_idx
        digits[x], digits[y] = digits[y], digits[x]
        return int(''.join(map(str, digits)))


def main():
    num = 2736
    assert Solution().maximumSwap(num) == 7236

    num = 9973
    assert Solution().maximumSwap(num) == 9973


if __name__ == '__main__':
    main()
