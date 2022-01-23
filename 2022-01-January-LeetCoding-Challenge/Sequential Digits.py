# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ''' BFS based solution. '''
        ans = list()
        for digit in range(1, 9):  # No digit greater than 9
            # Generate all sequential numbers starting with digit
            current_number = last_digit = digit
            while current_number <= high and last_digit <= 9:
                if current_number >= low:
                    ans.append(current_number)
                # Increment and append last digit to current number
                last_digit += 1
                current_number = current_number*10 + last_digit
        return sorted(ans)


def main():
    low, high = 100, 300
    assert Solution().sequentialDigits(low, high) == [123, 234]

    low, high = 1000, 13000
    assert Solution().sequentialDigits(low, high) == [1234, 2345, 3456, 4567,
                                                      5678, 6789, 12345]


if __name__ == '__main__':
    main()
