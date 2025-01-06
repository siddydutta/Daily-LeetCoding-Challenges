from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(map(int, boxes))
        n = len(boxes)
        left_moves, right_moves = [0] * n, [0] * n

        # compute weighted prefix and suffix sums
        count = boxes[0]
        for i in range(1, n):
            left_moves[i] = left_moves[i - 1] + count
            count += boxes[i]
        count = boxes[-1]
        for i in range(n - 2, -1, -1):
            right_moves[i] = right_moves[i + 1] + count
            count += boxes[i]
        return [l + r for l, r in zip(left_moves, right_moves)]


def main():
    boxes = '110'
    assert Solution().minOperations(boxes) == [1, 1, 3]

    boxes = '001011'
    assert Solution().minOperations(boxes) == [11, 8, 5, 4, 3, 4]


if __name__ == '__main__':
    main()
