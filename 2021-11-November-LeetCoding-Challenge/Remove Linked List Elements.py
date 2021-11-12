# -*- coding: utf-8 -*-
from typing import Optional


class ListNode:
    ''' Definition for singly-linked list. '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ptr = dummy

        while ptr and ptr.next:
            while ptr.next and ptr.next.val == val:
                ptr.next = ptr.next.next  # Skip the next node with val
            ptr = ptr.next

        return dummy.next


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    val = 6
    result = Solution().removeElements(head, val)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 5

    head = None
    val = 1
    assert not Solution().removeElements(head, val)

    head = ListNode(7)
    head.next = ListNode(7)
    head.next.next = ListNode(7)
    head.next.next.next = ListNode(7)
    val = 7
    assert not Solution().removeElements(head, val)


if __name__ == '__main__':
    main()
