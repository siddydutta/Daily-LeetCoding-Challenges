# -*- coding: utf-8 -*-
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nextt=None):
        self.val = val
        self.next = nextt


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> ListNode:
        # Count number of elements
        n, ptr = 0, head
        while ptr is not None:
            n += 1
            ptr = ptr.next

        # Find middle of linked list
        n, mid = n//2 if n % 2 != 0 else (n//2) - 1, head
        for _ in range(n):
            mid = mid.next

        # Reverse second half of linked list
        prev, curr = None, mid.next
        while curr is not None:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        mid.next = None

        # Merge lists
        head1, head2 = head, prev
        while head2 is not None:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt

        return head


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    result = Solution().reorderList(head)
    assert result.val == 1
    assert result.next.val == 4
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    result = Solution().reorderList(head)
    assert result.val == 1
    assert result.next.val == 5
    assert result.next.next.val == 2
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 3


if __name__ == '__main__':
    main()
