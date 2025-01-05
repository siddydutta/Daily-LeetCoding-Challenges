from itertools import accumulate
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # line sweep algorithm
        line = [0] * (len(s) + 1)  # account for shift after last element
        for start, end, direction in shifts:
            if direction == 1:
                # start shifting from start
                line[start] += 1
                # stop shifting after end
                line[end + 1] -= 1
            else:
                line[start] -= 1
                line[end + 1] += 1
        # prefix sum to calculate total shifts
        line = accumulate(line)

        result = ''
        for ch, sh in zip(s, line):
            result += chr(ord('a') + ((ord(ch) - ord('a') + sh) % 26))
        return result


def main():
    s = 'abc'
    shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    assert Solution().shiftingLetters(s, shifts) == 'ace'

    s = 'dztz'
    shifts = [[0, 0, 0], [1, 1, 1]]
    assert Solution().shiftingLetters(s, shifts) == 'catz'


if __name__ == '__main__':
    main()
