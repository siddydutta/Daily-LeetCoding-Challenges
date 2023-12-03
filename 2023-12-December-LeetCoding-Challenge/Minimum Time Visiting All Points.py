from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            (x2, y2), (x1, y1) = points[i], points[i-1]
            time += max(abs(x2-x1), abs(y2-y1))
        return time


def main():
    points = [[1, 1], [3, 4], [-1, 0]]
    assert Solution().minTimeToVisitAllPoints(points) == 7

    points = [[3, 2], [-2, 2]]
    assert Solution().minTimeToVisitAllPoints(points) == 5


if __name__ == '__main__':
    main()
