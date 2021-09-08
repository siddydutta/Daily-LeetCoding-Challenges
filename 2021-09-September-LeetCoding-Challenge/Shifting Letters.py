# -*- coding: utf-8 -*-
from itertools import accumulate
from typing import List


class Solution:
    '''
    Shift s[i] by sum(shift[i:]) times
    Time Complexity: O(n)
    '''
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # First i+1 letters are shifted shifts[i] times
        shifts.reverse()
        shifts = list(accumulate(shifts))  # Prefix sums on reversed shifts
        shifts.reverse()  # Reverse again for shifts for each position

        ans = ""
        for ch, shift in zip(s, shifts):
            ans += chr((ord(ch) - 97 + shift) % 26 + 97)

        return ans


def main():
    s = "abc"
    shifts = [3, 5, 9]
    assert Solution().shiftingLetters(s, shifts) == "rpl"

    s = "aaa"
    shifts = [1, 2, 3]
    assert Solution().shiftingLetters(s, shifts) == "gfd"


if __name__ == '__main__':
    main()
