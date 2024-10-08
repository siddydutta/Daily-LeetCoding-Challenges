class Solution:
    def minSwaps(self, s: str) -> int:
        open, close = 0, 0
        for ch in s:
            if ch == '[':
                open += 1
            elif open == 0:
                close += 1
            else:
                open -= 1
        # swaps to balance pairs
        return (close + 1) // 2


def main():
    s = '][]['
    assert Solution().minSwaps(s) == 1

    s = ']]][[['
    assert Solution().minSwaps(s) == 2


if __name__ == '__main__':
    main()
