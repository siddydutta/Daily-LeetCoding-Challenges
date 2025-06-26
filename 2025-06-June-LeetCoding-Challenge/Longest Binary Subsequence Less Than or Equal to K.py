class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        max_len, curr_sum = 0, 0
        for d in reversed(s):
            if d == '0':
                max_len += 1
            elif curr_sum + (1 << max_len) <= k:
                curr_sum += (1 << max_len)
                max_len += 1
        return max_len


def main():
    s = '1001010'
    k = 5
    assert Solution().longestSubsequence(s, k) == 5

    s = '00101001'
    k = 1
    assert Solution().longestSubsequence(s, k) == 6


if __name__ == '__main__':
    main()
