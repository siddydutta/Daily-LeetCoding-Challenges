class Solution:
    def maxScore(self, s: str) -> int:
        n1s = 0
        for ch in s:
            if ch == '1':
                n1s += 1

        n0s_left, n1s_right = 0, n1s
        max_score = float('-inf')
        for ch in s[:-1]:
            if ch == '0':
                n0s_left += 1
            elif ch == '1':
                n1s_right -= 1
            max_score = max(max_score, n0s_left+n1s_right)
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
