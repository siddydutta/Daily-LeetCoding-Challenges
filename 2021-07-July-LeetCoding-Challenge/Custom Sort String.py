# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    '''
    Hash table based solution.
    Time Complexity: O(n)
    '''
    def customSortString(self, order: str, string: str) -> str:
        ch_count = Counter(string)
        result = str()

        # First add all characters from string according to order
        for ch in order:
            try:
                result += ch * ch_count.pop(ch)
            except KeyError:
                continue

        # Add remaining characters from string that are not specified in order
        while ch_count:
            ch, count = ch_count.popitem()
            result += ch * count

        return result


def main():
    obj = Solution()
    order = "cba"
    string = "abcd"
    assert obj.customSortString(order, string) == "cbad"


if __name__ == '__main__':
    main()
