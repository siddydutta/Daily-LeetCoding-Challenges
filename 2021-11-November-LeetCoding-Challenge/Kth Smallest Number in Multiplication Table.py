# -*- coding: utf-8 -*-
class Solution:
    def isGreaterThanAtleastK(self, num: int, m: int, n: int, k: int) -> bool:
        ''' Returns if num is greater than *atleast* k elements. '''
        count = 0
        for row in range(1, m+1):
            vals = min(num//row, n)  # Count of numbers in row less than num
            if vals == 0:
                break
            count += vals
        return count >= k

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        ''' Binary search solution. '''
        left, right = 1, m*n
        while left < right:
            mid = left + (right-left) // 2
            if self.isGreaterThanAtleastK(mid, m, n, k):
                right = mid  # Converge to minimal solution
            else:
                left = mid + 1
        return left


def main():
    m, n, k = 3, 3, 5
    assert Solution().findKthNumber(m, n, k) == 3

    m, n, k = 2, 3, 6
    assert Solution().findKthNumber(m, n, k) == 6


if __name__ == '__main__':
    main()
