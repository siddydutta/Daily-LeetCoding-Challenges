from collections import defaultdict
from typing import List


class Solution:
    def buildMatrix(
            self,
            k: int,
            row_conditions: List[List[int]],
            col_conditions: List[List[int]]
    ) -> List[List[int]]:
        def dfs(
                src: int, adj: dict, visited: set, path: set, order: List[int]
        ) -> bool:
            if src in path:
                return False
            if src in visited:
                return True
            visited.add(src)
            path.add(src)
            for neighbour in adj[src]:
                if not dfs(neighbour, adj, visited, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges: List[List[int]]) -> List[int]:
            adj = defaultdict(list)
            for source, dest in edges:
                adj[source].append(dest)
            visited, path = set(), set()
            order = []
            for source in range(1, k+1):
                if not dfs(source, adj, visited, path, order):
                    return []
            return order[::-1]

        row_order = topo_sort(row_conditions)
        col_order = topo_sort(col_conditions)
        if not row_order or not col_order:
            return []  # cycle in the edges
        val_row_map = {num: pos for pos, num in enumerate(row_order)}
        val_col_map = {num: pos for pos, num in enumerate(col_order)}

        matrix = [[0]*k for _ in range(k)]
        for num in range(1, k+1):
            row, col = val_row_map[num], val_col_map[num]
            matrix[row][col] = num
        return matrix


def main():
    k = 3
    row_conds = [[1, 2], [3, 2]]
    col_conds = [[2, 1], [3, 2]]
    assert Solution().buildMatrix(k, row_conds, col_conds) == [[3, 0, 0],
                                                               [0, 0, 1],
                                                               [0, 2, 0]]

    k = 3
    row_conds = [[1, 2], [2, 3], [3, 1], [2, 3]]
    col_conds = [[2, 1]]
    assert Solution().buildMatrix(k, row_conds, col_conds) == []


if __name__ == '__main__':
    main()
