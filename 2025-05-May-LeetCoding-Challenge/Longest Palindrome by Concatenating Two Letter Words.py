from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        freq = Counter(words)
        length, centered = 0, False

        for word, count in freq.items():
            if word[0] == word[1]:
                if count % 2 == 0:
                    length += count
                else:
                    length += (count - 1)
                    centered = True
            elif word[0] < word[1]:
                length += 2 * min(count, freq[word[::-1]])

        length += centered
        return length * 2


def main():
    words = ['lc', 'cl', 'gg']
    assert Solution().longestPalindrome(words) == 6

    words = ['ab', 'ty', 'yt', 'lc', 'cl', 'ab']
    assert Solution().longestPalindrome(words) == 8

    words = ['cc', 'll', 'xx']
    assert Solution().longestPalindrome(words) == 2


if __name__ == '__main__':
    main()
