# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ''' Greedy and sorting based solution. '''
        people.sort(reverse=True)
        boats = int()

        while people:
            person1 = people.pop(0)  # Take heaviest at the time
            # Try to take lightest at the time
            if people and people[-1] + person1 <= limit:
                people.pop()
            boats += 1
        return boats


def main():
    people, limit = [1, 2], 3
    assert Solution().numRescueBoats(people, limit) == 1

    people, limit = [3, 2, 2, 1], 3
    assert Solution().numRescueBoats(people, limit) == 3

    people, limit = [3, 5, 3, 4], 5
    assert Solution().numRescueBoats(people, limit) == 4


if __name__ == '__main__':
    main()
