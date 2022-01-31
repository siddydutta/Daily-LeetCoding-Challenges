# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ''' Straightforward one-liner. '''
        return max([sum(customer) for customer in accounts])


def main():
    accounts = [[1, 2, 3],
                [3, 2, 1]]
    assert Solution().maximumWealth(accounts) == 6

    accounts = [[1, 5],
                [7, 3],
                [3, 5]]
    assert Solution().maximumWealth(accounts) == 10

    accounts = [[2, 8, 7],
                [7, 1, 3],
                [1, 9, 5]]
    assert Solution().maximumWealth(accounts) == 17


if __name__ == '__main__':
    main()
