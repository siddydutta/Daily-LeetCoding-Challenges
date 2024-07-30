class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b = 0
        cost = 0  # 1-D DP
        for ch in s:
            if ch == 'b':
                count_b += 1
            else:
                # remove all b's till now
                # or remove the a
                cost = min(cost+1, count_b)
        return cost


def main():
    s = 'aababbab'
    assert Solution().minimumDeletions(s) == 2

    s = 'bbaaaaabb'
    assert Solution().minimumDeletions(s) == 2


if __name__ == '__main__':
    main()
