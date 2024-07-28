from itertools import product
from math import inf
from typing import List


class Solution:
    def minimumCost(
            self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]
    ) -> int:
        # create matrix to store cost of converting ch1 -> ch2
        conv_matrix = [[inf]*26 for _ in range(26)]
        for i in range(26):
            conv_matrix[i][i] = 0
        for ch1, ch2, c in zip(original, changed, cost):
            ch1, ch2 = map(lambda ch: ord(ch)-97, (ch1, ch2))
            conv_matrix[ch1][ch2] = min(conv_matrix[ch1][ch2], c)
        # optimize matrix using floyd-warshall's algorithm
        for k in range(26):
            for i, j in product(range(26), range(26)):
                conv_matrix[i][j] = min(conv_matrix[i][j], conv_matrix[i][k]+conv_matrix[k][j])

        # compute total conversion cost
        total_cost = 0
        for s, t in zip(source, target):
            s, t = map(lambda ch: ord(ch)-97, (s, t))
            if conv_matrix[s][t] == inf:
                return -1
            total_cost += conv_matrix[s][t]
        return total_cost


def main():
    source = 'abcd'
    target = 'acbe'
    original = ['a', 'b', 'c', 'c', 'e', 'd']
    changed = ['b', 'c', 'b', 'e', 'b', 'e']
    cost = [2, 5, 5, 1, 2, 20]
    assert Solution().minimumCost(source, target, original, changed, cost) == 28

    source = 'aaaa'
    target = 'bbbb'
    original = ['a', 'c']
    changed = ['c', 'b']
    cost = [1, 2]
    assert Solution().minimumCost(source, target, original, changed, cost) == 12


if __name__ == '__main__':
    main()
