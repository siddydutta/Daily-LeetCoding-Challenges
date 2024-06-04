from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        single = False
        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                if not single:
                    # middle char
                    single = True
                    length += 1
                length += (count-1)
        return length


def main():
    s = 'abccccdd'
    assert Solution().longestPalindrome(s) == 7

    s = 'a'
    assert Solution().longestPalindrome(s) == 1

    s = 'ccc'
    assert Solution().longestPalindrome(s) == 3


if __name__ == '__main__':
    main()
