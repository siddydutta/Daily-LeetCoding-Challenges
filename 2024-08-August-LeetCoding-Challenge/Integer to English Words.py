ONES = ('', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
        'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
        'Seventeen', 'Eighteen', 'Nineteen',)
TENS = ('', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety',)
THOUSANDS = ('', 'Thousand', 'Million', 'Billion',)


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        def helper(num: int) -> str:
            if num == 0:
                return ''
            if num < 20:
                return ONES[num] + ' '
            if num < 100:
                return TENS[num//10] + ' ' + helper(num%10)
            return ONES[num//100] + ' Hundred ' + helper(num%100)

        i = 0
        words = ''
        while num > 0:
            if num % 1000 != 0:
                words = helper(num%1000) + THOUSANDS[i] + ' ' + words
            num //= 1000
            i += 1
        return words.strip()


def main():
    num = 123
    assert Solution().numberToWords(num) == 'One Hundred Twenty Three'

    num = 12345
    assert Solution().numberToWords(num) == 'Twelve Thousand Three Hundred Forty Five'

    num = 1234567
    assert Solution().numberToWords(num) == 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'


if __name__ == '__main__':
    main()
