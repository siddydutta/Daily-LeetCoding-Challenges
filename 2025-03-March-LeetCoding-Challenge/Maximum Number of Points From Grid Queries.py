from heapq import heappop, heappush


class Solution:
    DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        queries = [(query, idx) for idx, query in enumerate(queries)]
        queries.sort()
        rows, cols = len(grid), len(grid[0])
        result = [0] * len(queries)
        visited = [[False] * cols for _ in range(rows)]
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        points = 0
        for query, idx in queries:
            while heap and heap[0][0] < query:
                _, x, y = heappop(heap)
                points += 1
                for dx, dy in self.DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                        heappush(heap, (grid[nx][ny], nx, ny))
                        visited[nx][ny] = True
            result[idx] = points
        return result


def main():
    grid = [[1, 2, 3],
            [2, 5, 7],
            [3, 5, 1]]
    queries = [5, 6, 2]
    assert Solution().maxPoints(grid, queries) == [5, 8, 1]

    grid = [[5, 2, 1],
            [1, 1, 2]]
    queries = [3]
    assert Solution().maxPoints(grid, queries) == [0]


if __name__ == '__main__':
    main()
