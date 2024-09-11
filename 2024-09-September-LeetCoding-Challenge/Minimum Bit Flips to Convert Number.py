class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()


def main():
    start = 10
    goal = 7
    assert Solution().minBitFlips(start, goal) == 3

    start = 3
    goal = 4
    assert Solution().minBitFlips(start, goal) == 3


if __name__ == '__main__':
    main()
