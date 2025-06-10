from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd, min_even = 0, float('inf')
        for value in freq.values():
            if value & 1:
                max_odd = max(max_odd, value)
            else:
                min_even = min(min_even, value)
        return max_odd - min_even


def main():
    s = 'aaaaabbc'
    assert Solution().maxDifference(s) == 3

    s = 'abcabcab'
    assert Solution().maxDifference(s) == 1


if __name__ == '__main__':
    main()
