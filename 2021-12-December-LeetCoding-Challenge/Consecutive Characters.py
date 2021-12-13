# -*- coding: utf-8 -*-
class Solution:
    def maxPower(self, s: str) -> int:
        ''' Straight-forward solution. '''
        power, current = 1, 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current += 1
            else:
                power = max(power, current)
                current = 1  # Reset

        power = max(power, current)  # If consecutive is at end of string
        return power


def main():
    s = "leetcode"
    assert Solution().maxPower(s) == 2

    s = "abbcccddddeeeeedcba"
    assert Solution().maxPower(s) == 5

    s = "triplepillooooow"
    assert Solution().maxPower(s) == 5

    s = "hooraaaaaaaaaaay"
    assert Solution().maxPower(s) == 11

    s = "tourist"
    assert Solution().maxPower(s) == 1


if __name__ == '__main__':
    main()
