from itertools import product
from typing import List


DIFF = ((-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1))


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        image = [[None] * cols for _ in range(rows)]
        for x, y in product(range(rows), range(cols)):
            neighbours = list()
            for dx, dy in DIFF:
                if 0 <= x+dx < rows and 0 <= y+dy < cols:
                    neighbours.append(img[x+dx][y+dy])
            image[x][y] = sum(neighbours) // len(neighbours)
        return image


def main():
    img = [[1, 1, 1],
           [1, 0, 1],
           [1, 1, 1]]
    assert Solution().imageSmoother(img) == [[0, 0, 0],
                                             [0, 0, 0],
                                             [0, 0, 0]]

    img = [[100, 200, 100],
           [200, 50, 200],
           [100, 200, 100]]
    assert Solution().imageSmoother(img) == [[137, 141, 137],
                                             [141, 138, 141],
                                             [137, 141, 137]]


if __name__ == '__main__':
    main()
