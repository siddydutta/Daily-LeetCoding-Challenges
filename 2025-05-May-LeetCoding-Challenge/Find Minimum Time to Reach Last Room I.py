from heapq import heappop, heappush


class Solution:
    DIRS = ((0, -1), (0, 1), (1, 0), (-1, 0))

    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        """Dijkstra's algorithm-based implementation."""
        n, m = len(moveTime), len(moveTime[0])
        visited = {(0, 0)}
        heap = [(0, (0, 0))]  # time, (x, y)
        while heap:
            time, (x, y) = heappop(heap)
            if x == n - 1 and y == m - 1:
                return time
            for dx, dy in self.DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    leave_time = max(moveTime[nx][ny], time) + 1
                    heappush(heap, (leave_time, (nx, ny)))
                    visited.add((nx, ny))
        return 0


def main():
    moveTime = [[0, 4],
                [4, 4]]
    assert Solution().minTimeToReach(moveTime) == 6

    moveTime = [[0, 0, 0],
                [0, 0, 0]]
    assert Solution().minTimeToReach(moveTime) == 3


if __name__ == '__main__':
    main()
