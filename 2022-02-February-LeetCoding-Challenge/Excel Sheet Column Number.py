# -*- coding: utf-8 -*-
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ''' Math based solution. '''
        result = int()
        for ch in columnTitle:
            digit = ord(ch) - 64
            result = result*26 + digit
        return result


def main():
    columnTitle = "A"
    assert Solution().titleToNumber(columnTitle) == 1

    columnTitle = "AB"
    assert Solution().titleToNumber(columnTitle) == 28

    columnTitle = "ZY"
    assert Solution().titleToNumber(columnTitle) == 701


if __name__ == '__main__':
    main()
