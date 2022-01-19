# -*- coding: utf-8 -*-
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        First uses Floyd's circle finding algorithm to check if cycle exists.
        If cycle exists, then initializes two pointers.
        ptr1 is meant to be pos while ptr2 cycles until it reaches ptr1.
        ptr1 is incremented if ptr2 doesn't reach it.
        '''
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle exists
                ptr1, ptr2 = head, slow
                while ptr1 != ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                return ptr1
        return None


def main():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    assert Solution().detectCycle(head) == head.next

    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = head
    assert Solution().detectCycle(head) == head

    head = ListNode(1)
    assert Solution().detectCycle(head) is None


if __name__ == '__main__':
    main()
