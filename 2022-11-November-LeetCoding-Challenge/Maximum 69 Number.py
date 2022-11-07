class Solution:
    def maximum69Number(self, num: int) -> int:
        number = str(num)
        for idx, digit in enumerate(number):
            if digit == '6':
                # replace first instance of 6 with 9
                return int(number[:idx] + '9' + number[idx+1:])
        return int(number)  # no 6 present, number is max
        # return int(str(num).replace('6', '9', 1))


def main():
    num = 9669
    assert Solution().maximum69Number(num) == 9969

    num = 9996
    assert Solution().maximum69Number(num) == 9999

    num = 9999
    assert Solution().maximum69Number(num) == 9999


if __name__ == '__main__':
    main()
