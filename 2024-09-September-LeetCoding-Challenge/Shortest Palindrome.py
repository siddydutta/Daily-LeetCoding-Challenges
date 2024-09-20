class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # find longest prefix suffix array
        # using KMP algorithm
        pattern = s + '#' + s[::-1]
        lps = [0] * len(pattern)
        length = 0
        ptr = 1
        while ptr < len(pattern):
            if pattern[ptr] == pattern[length]:
                # match found
                lps[ptr] = length + 1  # length of arr
                length += 1
                ptr += 1
            else:
                if length == 0:
                    # start ptr again
                    lps[ptr] = 0
                    ptr += 1
                else:
                    # skip comparisons
                    length = lps[length-1]
        # last LPS is the length of the longest
        # palindromic prefix of s
        idx = lps[-1]
        return s[idx:][::-1] + s


def main():
    s = 'aacecaaa'
    assert Solution().shortestPalindrome(s) == 'aaacecaaa'

    s = 'abcd'
    assert Solution().shortestPalindrome(s) == 'dcbabcd'


if __name__ == '__main__':
    main()
