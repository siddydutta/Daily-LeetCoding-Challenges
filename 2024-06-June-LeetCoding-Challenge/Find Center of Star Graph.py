from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # return common node from first two edges
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]


def main():
    edges = [[1, 2], [2, 3], [4, 2]]
    assert Solution().findCenter(edges) == 2

    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    assert Solution().findCenter(edges) == 1


if __name__ == '__main__':
    main()
