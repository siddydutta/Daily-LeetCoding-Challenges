# -*- coding: utf-8 -*-
class Solution:
    def rectangleArea(self, rectangles):
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        ys = sorted(set([y for x1, y1, x2, y2 in rectangles for y in [y1, y2]]))
        x_i = {x: index for index, x in enumerate(xs)}
        y_i = {y: index for index, y in enumerate(ys)}

        m, n = len(y_i), len(x_i)
        grid = [[0] * m for _ in range(n)]
        for x1, y1, x2, y2 in rectangles:
            for x in range(x_i[x1], x_i[x2]):
                for y in range(y_i[y1], y_i[y2]):
                    grid[x][y] = 1

        total_area = 0
        for x in range(n-1):
            for y in range(m-1):
                total_area += grid[x][y] * (xs[x+1] - xs[x]) * (ys[y+1] - ys[y])
        return total_area % (10**9 + 7)


def main():
    rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    assert Solution().rectangleArea(rectangles) == 6

    rectangles = [[0, 0, 1000000000, 1000000000]]
    assert Solution().rectangleArea(rectangles) == 49


if __name__ == '__main__':
    main()
