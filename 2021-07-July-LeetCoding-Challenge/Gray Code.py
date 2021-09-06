# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Simple Bit Manipulation
    Time Complexity: O(2^n)
    '''
    def grayCode(self, n: int) -> List[int]:
        answer = list()
        for i in range(2**n):
            answer.append(i ^ (i//2))  # XOR based solution
        return answer


def main():
    obj = Solution()
    assert obj.grayCode(1) == [0, 1]
    assert obj.grayCode(2) == [0, 1, 3, 2]


if __name__ == '__main__':
    main()
