from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for key, value in freq.items():
            if value == 1:
                k -= 1
            if k == 0:
                return key
        return ''


def main():
    arr = ['d', 'b', 'c', 'b', 'c', 'a']
    k = 2
    assert Solution().kthDistinct(arr, k) == 'a'

    arr = ['aaa', 'aa', 'a']
    k = 1
    assert Solution().kthDistinct(arr, k) == 'aaa'

    arr = ['a', 'b', 'a']
    k = 3
    assert Solution().kthDistinct(arr, k) == ''


if __name__ == '__main__':
    main()
