from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players, loss_counts = set(), defaultdict(int)
        for winner, looser in matches:
            players.add(winner)
            players.add(looser)
            loss_counts[looser] += 1
        answer = [[], []]
        for player in players:
            count = loss_counts[player]
            if count in {0, 1}:
                answer[count].append(player)
        return list(map(list, map(sorted, answer)))


def main():
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9],
               [10, 4], [10, 9]]
    assert Solution().findWinners(matches) == [[1, 2, 10], [4, 5, 7, 8]]

    matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
    assert Solution().findWinners(matches) == [[1, 2, 5, 6], []]


if __name__ == '__main__':
    main()
