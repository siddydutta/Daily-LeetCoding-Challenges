# -*- coding: utf-8 -*-


class Solution:
    def partitionString(self, s: str) -> int:
        count, seen = 0, set()
        for ch in s:
            if ch in seen:
                count += 1
                seen.clear()
            seen.add(ch)
        return count + 1


def main():
    s = "abacaba"
    assert Solution().partitionString(s) == 4

    s = "ssssss"
    assert Solution().partitionString(s) == 6


if __name__ == '__main__':
    main()
