class Solution:
    def minimumSteps(self, s: str) -> int:
        n_ones = 0
        swaps = 0
        for ch in s:
            if ch == '1':
                n_ones += 1
            else:
                swaps += n_ones
        return swaps


def main():
    s = '101'
    assert Solution().minimumSteps(s) == 1

    s = '100'
    assert Solution().minimumSteps(s) == 2

    s = '0111'
    assert Solution().minimumSteps(s) == 0


if __name__ == '__main__':
    main()
