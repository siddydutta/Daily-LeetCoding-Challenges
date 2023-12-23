class Solution:
    def isPathCrossing(self, path: str) -> bool:
        DIFF = {'N': (0, 1),
                'S': (0, -1),
                'E': (1, 0),
                'W': (-1, 0)}

        x, y = 0, 0
        visited = {(x, y)}
        for d in path:
            dx, dy = DIFF[d]
            x, y = x+dx, y+dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


def main():
    path = 'NES'
    assert not Solution().isPathCrossing(path)

    path = 'NESWW'
    assert Solution().isPathCrossing(path)

    path = 'SS'
    assert not Solution().isPathCrossing(path)


if __name__ == '__main__':
    main()
