# -*- coding: utf-8 -*-
from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


def main():
    n = 3
    assert Solution().bulbSwitch(n) == 1

    n = 0
    assert Solution().bulbSwitch(n) == 0

    n = 1
    assert Solution().bulbSwitch(n) == 1

    n = 9999999
    assert Solution().bulbSwitch(n) == 3162


if __name__ == '__main__':
    main()
