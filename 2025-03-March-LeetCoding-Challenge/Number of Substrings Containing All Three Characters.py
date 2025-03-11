class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ch_map = {ch: 0 for ch in ['a', 'b', 'c']}
        left_ptr = 0
        ans = 0
        for right_ptr in range(n):
            ch_map[s[right_ptr]] += 1
            while ch_map['a'] and ch_map['b'] and ch_map['c']:
                ans += (n - right_ptr)
                ch_map[s[left_ptr]] -= 1
                left_ptr += 1
        return ans


def main():
    s = 'abcabc'
    assert Solution().numberOfSubstrings(s) == 10

    s = 'aaacb'
    assert Solution().numberOfSubstrings(s) == 3


if __name__ == '__main__':
    main()
