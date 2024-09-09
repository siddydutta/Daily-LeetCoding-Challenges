from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(
            self, m: int, n: int, head: Optional[ListNode]
    ) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        d = directions[0]

        x, y = 0, 0
        min_row, min_col = 0, 0
        max_row, max_col = m-1, n-1

        while head is not None:
            matrix[x][y] = head.val
            head = head.next

            if y == max_col and d == directions[0]:
                # change direction to down
                d = directions[1]
                min_row += 1
            if x == max_row and d == directions[1]:
                # change direction to left
                d = directions[2]
                max_col -= 1
            if y == min_col and d == directions[2]:
                # change direction to up
                d = directions[3]
                max_row -= 1
            if x == min_row and d == directions[3]:
                # change direction to right
                d = directions[0]
                min_col += 1
            x += d[0]
            y += d[1]

        return matrix


def main():
    m = 3
    n = 5
    head = ListNode(3)
    head.next = ListNode(0)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(6)
    head.next.next.next.next = ListNode(8)
    head.next.next.next.next.next = ListNode(1)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
    assert Solution().spiralMatrix(m, n, head) == [[3, 0, 2, 6, 8],
                                                   [5, 0, -1, -1, 1],
                                                   [5, 2, 4, 9, 7]]

    m = 1
    n = 4
    head = ListNode(0, ListNode(1, ListNode(2)))
    assert Solution().spiralMatrix(m, n, head) == [[0, 1, 2, -1]]


if __name__ == '__main__':
    main()
