# -*- coding: utf-8 -*-
class Solution:
    def champagneTower(self, poured: int, query_row: int,
                       query_glass: int) -> float:
        if poured == 0:
            return 0
        if query_row == 0:
            return 1

        current = [poured]
        for row in range(1, query_row+1):
            nextt = [0] * (row+1)
            for i in range(len(current)):
                remaining = current[i] - 1
                if remaining < 0.0:
                    continue

                nextt[i] += remaining / 2
                nextt[i+1] += remaining / 2
            current = nextt

        return min(nextt[query_glass], 1)


def main():
    poured, query_row, query_glass = 1, 1, 1
    assert Solution().champagneTower(poured, query_row, query_glass) == 0.0

    poured, query_row, query_glass = 2, 1, 1
    assert Solution().champagneTower(poured, query_row, query_glass) == 0.50000

    poured, query_row, query_glass = 100000009, 33, 17
    assert Solution().champagneTower(poured, query_row, query_glass) == 1.00000


if __name__ == '__main__':
    main()
