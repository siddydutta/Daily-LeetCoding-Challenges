# -*- coding: utf-8 -*-
from typing import List
from queue import Queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)  # For constant lookups
        queue = Queue()
        visited = set()
        moves = 0

        # Initial position
        queue.put("0000")
        visited.add("0000")

        # Breadth first search at every level to eval lock positions
        while not queue.empty():
            # Explore lock positions at current level
            for _ in range(queue.qsize()):
                lock = queue.get()  # Current lock position
                # If lock combination is a deadend
                if lock in deadends:
                    continue
                # If lock combination is the target
                if lock == target:
                    return moves

                # Else add all next combinations to queue for next level
                for i in range(4):
                    digit = lock[i]
                    # Increment digit
                    s1 = lock[0:i] + str((int(digit) + 1) % 10) + lock[i+1:]
                    if s1 not in visited and s1 not in deadends:
                        queue.put(s1)
                        visited.add(s1)
                    # Decrement digit
                    s2 = lock[0:i] + str((int(digit) - 1) % 10) + lock[i+1:]
                    if s2 not in visited and s2 not in deadends:
                        queue.put(s2)
                        visited.add(s2)
            moves += 1
        return -1


if __name__ == '__main__':
    obj = Solution()
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    moves = obj.openLock(deadends, target)
    assert moves == 6

    deadends = ["8888"]
    target = "0009"
    moves = obj.openLock(deadends, target)
    assert moves == 1

    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    moves = obj.openLock(deadends, target)
    assert moves == -1
