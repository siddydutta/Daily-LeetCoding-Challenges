from typing import List


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 2:
            return points

        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1])-(b[0]-o[0])*(a[1]-o[1])

        points.sort()
        upper = []
        for p in points:
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) > 0:
                upper.pop()
            upper.append(p)

        lower = []
        for p in reversed(points):
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) > 0:
                lower.pop()
            lower.append(p)
        return list(map(list, set(map(tuple, lower[:-1] + upper[:-1]))))


def main():
    points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
    assert sorted(Solution().outerTrees(points)) \
        == sorted([[1, 1], [2, 0], [3, 3], [2, 4], [4, 2]])

    points = [[1, 2], [2, 2], [4, 2]]
    assert sorted(Solution().outerTrees(points)) \
        == sorted([[4, 2], [2, 2], [1, 2]])


if __name__ == '__main__':
    main()
