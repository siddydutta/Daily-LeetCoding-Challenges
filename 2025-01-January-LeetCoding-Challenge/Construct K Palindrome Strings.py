from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        n_odds = sum(c & 1 for c in Counter(s).values())
        return n_odds <= k


def main():
    s = 'annabelle'
    k = 2
    assert Solution().canConstruct(s, k) is True

    s = 'leetcode'
    k = 3
    assert Solution().canConstruct(s, k) is False

    s = 'true'
    k = 4
    assert Solution().canConstruct(s, k) is True


if __name__ == '__main__':
    main()
