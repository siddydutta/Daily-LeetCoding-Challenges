from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        counts = defaultdict(int)
        pairs = 0
        for domino in map(tuple, (map(sorted, dominoes))):
            pairs += counts[domino]
            counts[domino] += 1
        return pairs


def main():
    dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
    assert Solution().numEquivDominoPairs(dominoes) == 1

    dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    assert Solution().numEquivDominoPairs(dominoes) == 3


if __name__ == '__main__':
    main()
