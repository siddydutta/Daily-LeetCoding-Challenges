# -*- coding: utf-8 -*-
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' Insertion sort with a linked list. '''
        dummy = ListNode()  # Dummy head
        prev = dummy  # Prev is the last node in the sorted list

        while head is not None:
            temp = head.next  # Maintain temp to continue with linked list
            # First check if last sorted element is greater than current
            if prev.val >= head.val:
                prev = dummy  # Start comparing from first
            # Move pointer to find appropriate insert position
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            # Insert the unsorted node (after prev)
            head.next = prev.next
            prev.next = head  # Not necessarily setting prev to last sorted
            head = temp  # Continue with next unsorted element

        return dummy.next


def main():
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    res = Solution().insertionSortList(head)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 3
    assert res.next.next.next.val == 4

    head = ListNode(-1)
    head.next = ListNode(5)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(0)
    res = Solution().insertionSortList(head)
    assert res.val == -1
    assert res.next.val == 0
    assert res.next.next.val == 3
    assert res.next.next.next.val == 4
    assert res.next.next.next.next.val == 5


if __name__ == '__main__':
    main()
