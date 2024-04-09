from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                # people till k will appear max x[i] or x[k]
                time += min(tickets[i], tickets[k])
            else:
                # people after k will appear max x[i] or x[k]-1
                # x[k]-1 is the number of ops because of rotation
                time += min(tickets[i], tickets[k]-1)
        return time


def main():
    tickets = [2, 3, 2]
    k = 2
    assert Solution().timeRequiredToBuy(tickets, k) == 6

    tickets = [5, 1, 1, 1]
    k = 0
    assert Solution().timeRequiredToBuy(tickets, k) == 8


if __name__ == '__main__':
    main()
