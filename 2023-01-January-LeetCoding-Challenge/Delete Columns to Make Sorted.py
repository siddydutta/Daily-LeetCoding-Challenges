# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1
                    break
        return count


def main():
    strs = ["cba", "daf", "ghi"]
    assert Solution().minDeletionSize(strs) == 1

    strs = ["a", "b"]
    assert Solution().minDeletionSize(strs) == 0

    strs = ["zyx", "wvu", "tsr"]
    assert Solution().minDeletionSize(strs) == 3


if __name__ == '__main__':
    main()
