class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()

        def dfs(sequence: str, remaining: str) -> None:
            nonlocal result
            if sequence in result:
                return
            result.add(sequence)
            for i in range(len(remaining)):
                dfs(sequence+remaining[i], remaining[:i]+remaining[i+1:])
        dfs(str(), tiles)
        return len(result) - 1


def main():
    tiles = 'AAB'
    assert Solution().numTilePossibilities(tiles) == 8

    tiles = 'AAABBC'
    assert Solution().numTilePossibilities(tiles) == 188

    tiles = 'V'
    assert Solution().numTilePossibilities(tiles) == 1


if __name__ == '__main__':
    main()
