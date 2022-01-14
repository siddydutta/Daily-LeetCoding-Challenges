# -*- coding: utf-8 -*-
class Solution:
    def myAtoi(self, s: str) -> int:
        ''' Straight-forward solution. '''
        val = 2**31
        min_val, max_val = -val, val-1
        s = s.strip()  # Remove whitespaces
        if len(s) == 0:
            return 0

        # Check for initial sign
        is_negative = False
        if s[0] == '-':
            is_negative = True
            ptr = 1
        elif s[0] == '+':
            ptr = 1
        else:
            ptr = 0

        # Get numeric value
        number = ""
        while(ptr < len(s) and s[ptr].isdigit()):
            number += s[ptr]
            ptr += 1
        if len(number) == 0:
            return 0
        else:
            number = int(number)

        # Change sign and clamp the integer
        if is_negative:
            number = -number
        number = min(max_val, number)
        number = max(min_val, number)
        return number


def main():
    s = "42"
    assert Solution().myAtoi(s) == 42

    s = "   -42"
    assert Solution().myAtoi(s) == -42

    s = "4193 with words"
    assert Solution().myAtoi(s) == 4193


if __name__ == '__main__':
    main()
