# -*- coding: utf-8 -*-
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' Solution using two-pointers. '''
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # Fast moves at double slow's pace
        # Once fast has reached the end, slow has only reached the middle
        return slow


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    assert Solution().middleNode(head) == head.next.next

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    assert Solution().middleNode(head) == head.next.next.next


if __name__ == '__main__':
    main()
