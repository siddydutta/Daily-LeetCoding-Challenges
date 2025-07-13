class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        ptr1, ptr2 = 0, 0
        while ptr1 < len(players) and ptr2 < len(trainers):
            if players[ptr1] <= trainers[ptr2]:
                ptr1 += 1
            ptr2 += 1
        return ptr1


def main():
    players = [4, 7, 9]
    trainers = [8, 2, 5, 8]
    assert Solution().matchPlayersAndTrainers(players, trainers) == 2

    players = [1, 1, 1]
    trainers = [10]
    assert Solution().matchPlayersAndTrainers(players, trainers) == 1


if __name__ == '__main__':
    main()
