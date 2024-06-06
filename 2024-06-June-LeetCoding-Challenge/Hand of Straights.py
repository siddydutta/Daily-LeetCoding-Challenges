from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        heapify(hand)
        while hand:
            start = heappop(hand)
            if freq[start] == 0:
                # already used
                continue
            freq[start] -= 1
            # check k consecutive
            for i in range(1, groupSize):
                if freq[start+i] == 0:
                    return False
                freq[start+i] -= 1
        return True


def main():
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    assert Solution().isNStraightHand(hand, groupSize) is True

    hand = [1, 2, 3, 4, 5]
    groupSize = 4
    assert Solution().isNStraightHand(hand, groupSize) is False


if __name__ == '__main__':
    main()
