# -*- coding: utf-8 -*-
from typing import List


class NaiveSolution:
    def maxArea(self, h: int, w: int,
                horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Add border values as cuts
        horizontalCuts += [0, h]
        verticalCuts += [0, w]

        # Sort cuts
        horizontalCuts.sort()
        verticalCuts.sort()

        # Calculate area of each cut
        # Results in -> O(len(horizontalCuts)*len(verticalCuts))
        maxArea = int()
        for i in range(1, len(horizontalCuts)):
            for j in range(1, len(verticalCuts)):
                height = horizontalCuts[i] - horizontalCuts[i-1]
                breadth = verticalCuts[j] - verticalCuts[j-1]
                area = height * breadth
                maxArea = max(maxArea, area)

        return maxArea % (10**9 + 7)


class Solution:
    def __maxDifferenceConsecutiveElements(self, array: List[int]) -> int:
        '''
        Returns the maximum difference between consecutive elements in a
        *sorted* array.
        '''
        maxDifference = int()
        for index in range(1, len(array)):
            difference = array[index] - array[index-1]
            maxDifference = max(maxDifference, difference)
        return maxDifference

    def maxArea(self, h: int, w: int,
                horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Add border values as cuts
        horizontalCuts += [0, h]
        verticalCuts += [0, w]

        # Sort cuts
        horizontalCuts.sort()
        verticalCuts.sort()

        # Get maximum differences for each dimension
        hDiff = self.__maxDifferenceConsecutiveElements(horizontalCuts)
        vDiff = self.__maxDifferenceConsecutiveElements(verticalCuts)

        # Maximum area is product of height and breadth
        return (hDiff * vDiff) % (10**9 + 7)


if __name__ == '__main__':
    obj = Solution()
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]
    assert obj.maxArea(h, w, horizontalCuts, verticalCuts) == 4

    horizontalCuts = [3, 1]
    verticalCuts = [1]
    assert obj.maxArea(h, w, horizontalCuts, verticalCuts) == 6

    horizontalCuts = [3]
    verticalCuts = [3]
    assert obj.maxArea(h, w, horizontalCuts, verticalCuts) == 9
