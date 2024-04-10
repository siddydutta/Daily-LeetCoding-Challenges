from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        res = [None] * n
        idx = 0
        flag = False
        while deck:
            if res[idx] is not None:
                idx = (idx+1) % n
                continue
            if not flag:
                res[idx] = deck.pop(0)
            flag = not flag
            idx = (idx+1) % n
        return res


def main():
    deck = [17, 13, 11, 2, 3, 5, 7]
    assert Solution().deckRevealedIncreasing(deck) == [2, 13, 3, 11, 5, 17, 7]

    deck = [1, 1000]
    assert Solution().deckRevealedIncreasing(deck) == [1, 1000]


if __name__ == '__main__':
    main()
