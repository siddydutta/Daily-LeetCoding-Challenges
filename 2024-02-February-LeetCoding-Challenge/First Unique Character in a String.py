from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = Counter(s)
        for index, ch in enumerate(s):
            if frequency.get(ch) == 1:
                return index
        return -1


def main():
    s = 'leetcode'
    assert Solution().firstUniqChar(s) == 0

    s = 'loveleetcode'
    assert Solution().firstUniqChar(s) == 2

    s = 'aabb'
    assert Solution().firstUniqChar(s) == -1


if __name__ == '__main__':
    main()
