from collections import deque


class Solution:
    def maxCandies(
            self,
            status: list[int],
            candies: list[int],
            keys: list[list[int]],
            containedBoxes: list[list[int]],
            initialBoxes: list[int]) -> int:
        queue = deque([])
        # store flags if reachable but unopened
        boxes = [False] * len(status)
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
            else:
                boxes[box] = True
        count = 0
        while queue:
            box = queue.popleft()
            count += candies[box]
            for i in keys[box]:
                if status[i] == 0 and boxes[i] is True:
                    queue.append(i)
                status[i] = 1
            for i in containedBoxes[box]:
                if status[i] == 1:
                    queue.append(i)
                else:
                    boxes[i] = True
        return count


def main():
    status = [1, 0, 1, 0]
    candies = [7, 5, 4, 100]
    keys = [[], [], [1], []]
    containedBoxes = [[1, 2], [3], [], []]
    initialBoxes = [0]
    assert Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes) == 16

    status = [1, 0, 0, 0, 0, 0]
    candies = [1, 1, 1, 1, 1, 1]
    keys = [[1, 2, 3, 4, 5], [], [], [], [], []]
    containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []]
    initialBoxes = [0]
    assert Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes) == 6


if __name__ == '__main__':
    main()
