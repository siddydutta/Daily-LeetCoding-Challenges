# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, current = 0, 0
        start = 0
        for i in range(len(gas)):
            current = current + gas[i] - cost[i]
            total = total + gas[i] - cost[i]
            if current < 0:
                current = 0
                start = i + 1

        if total >= 0:
            return start
        else:
            return -1


def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert Solution().canCompleteCircuit(gas, cost) == 3

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    assert Solution().canCompleteCircuit(gas, cost) == -1


if __name__ == '__main__':
    main()
