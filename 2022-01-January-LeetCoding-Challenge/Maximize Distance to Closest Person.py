# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        One-pass, two-pointer based solution.
        Idea is to find the maximum distance between two occupied seats.
        The answer will be half of that maximum distance.
        Time Complexity: O(n)
        '''
        left = -1  # Pointer to last taken index
        max_dist = 0  # To mainain maxdistance between two taken indices
        for index, seat in enumerate(seats):
            if seat == 0:
                continue  # Keep going forward
            if left == -1:
                # First taken seat, max distance is equal to index
                max_dist = index
            else:
                # Update max distance for subsequent taken seats
                max_dist = max(max_dist, (index-left)//2)
            left = index  # Update pointer to latest taken seat
        if seats[-1] == 0:
            # Edge case when last seat is not taken, recompute max distance
            max_dist = max(max_dist, len(seats)-1-left)
        return max_dist


def main():
    seats = [1, 0, 0, 0, 1, 0, 1]
    assert Solution().maxDistToClosest(seats) == 2

    seats = [1, 0, 0, 0]
    assert Solution().maxDistToClosest(seats) == 3

    seats = [0, 1]
    assert Solution().maxDistToClosest(seats) == 1


if __name__ == '__main__':
    main()
