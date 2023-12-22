class Solution:
    def maxScore(self, s: str) -> int:
        zeroes, ones = 0, s.count('1')
        max_score = float('-inf')
        for ch in s[:-1]:
            if ch == '0':
                zeroes += 1
            elif ch == '1':
                ones -= 1
            max_score = max(max_score, zeroes+ones)
        return max_score


def main():
    s = '011101'
    assert Solution().maxScore(s) == 5

    s = '00111'
    assert Solution().maxScore(s) == 5

    s = '1111'
    assert Solution().maxScore(s) == 3


if __name__ == '__main__':
    main()
