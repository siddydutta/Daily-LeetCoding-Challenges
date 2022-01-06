# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ''' Cumulative sum using hashmap based solution. '''
        locations = defaultdict(int)  # Count of people at each location
        for people, start, end in trips:
            locations[start] += people  # People on board
            locations[end] -= people  # People offboard

        passengers = 0
        for loc in sorted(locations):
            # Starting from initial, check capacity at each location
            passengers += locations[loc]
            if passengers > capacity:
                return False
        return True


def main():
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    assert not Solution().carPooling(trips, capacity)

    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 5
    assert Solution().carPooling(trips, capacity)


if __name__ == '__main__':
    main()
