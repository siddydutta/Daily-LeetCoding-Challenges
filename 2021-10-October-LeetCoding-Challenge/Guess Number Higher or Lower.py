# -*- coding: utf-8 -*-
from typing import Callable


class Solution:
    ''' Binary search based solution. '''
    def guessNumber(self, n: int, guess: Callable) -> int:
        '''
        Parameters
        ----------
        guess : Callable
            pre-defined guess API, passed as a parameter for this case.
        '''
        first, last = 1, n
        while first <= last:
            mid = (first + last) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == 1:
                first = mid + 1
            elif res == -1:
                last = mid - 1
        return  # Dummy return


def main():
    examples = [(10, 6), (1, 1), (2, 1), (2, 2)]
    for n, pick in examples:
        guess_api = lambda x: 0 if x == pick else 1 if pick > x else -1
        assert Solution().guessNumber(n, guess_api) == pick


if __name__ == '__main__':
    main()
