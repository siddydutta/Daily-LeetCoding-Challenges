class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black, max_black = 0, 0
        for idx in range(len(blocks)):
            black += blocks[idx] == 'B'
            if idx >= k:
                black -= blocks[idx-k] == 'B'
            max_black = max(max_black, black)
        return k - max_black


def main():
    blocks = 'WBBWWBBWBW'
    k = 7
    assert Solution().minimumRecolors(blocks, k) == 3

    blocks = 'WBWBBBW'
    k = 2
    assert Solution().minimumRecolors(blocks, k) == 0


if __name__ == '__main__':
    main()
