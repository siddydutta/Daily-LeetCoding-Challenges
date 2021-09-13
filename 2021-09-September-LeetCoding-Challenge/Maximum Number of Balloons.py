# -*- coding: utf-8 -*-
from math import inf
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        frequency = Counter(text)
        max_balloons = inf

        for ch in 'balon':
            if ch == 'l' or ch == 'o':
                max_balloons = min(max_balloons, frequency.get(ch, 0) // 2)
            else:
                max_balloons = min(max_balloons, frequency.get(ch, 0))

        return max_balloons


def main():
    text = "nlaebolko"
    assert Solution().maxNumberOfBalloons(text) == 1

    text = "loonbalxballpoon"
    assert Solution().maxNumberOfBalloons(text) == 2

    text = "leetcode"
    assert Solution().maxNumberOfBalloons(text) == 0


if __name__ == '__main__':
    main()
