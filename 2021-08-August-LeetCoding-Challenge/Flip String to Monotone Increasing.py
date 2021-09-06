# -*- coding: utf-8 -*-
class Solution:
    '''
    Dynamic programming based solution.
    Time Complexity: O(n)
    '''
    def minFlipsMonoIncr(self, s: str) -> int:
        n_ones = 0  # Count of 1s
        n_flips = 0  # Count of flips

        for ch in s:
            if ch == '1':
                n_ones += 1
            else:
                # Is it better to flip the next digit or flip previous ones
                n_flips = min(n_ones, n_flips+1)

        return n_flips


def main():
    s = "00110"
    assert Solution().minFlipsMonoIncr(s) == 1

    s = "010110"
    assert Solution().minFlipsMonoIncr(s) == 2

    s = "00011000"
    assert Solution().minFlipsMonoIncr(s) == 2


if __name__ == '__main__':
    main()
