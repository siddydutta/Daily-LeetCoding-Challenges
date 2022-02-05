# -*- coding: utf-8 -*-
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        ''' Merges two linked lists. '''
        dummy = ptr = ListNode()
        while left is not None and right is not None:
            if left.val < right.val:
                ptr.next = left
                left = left.next
            else:
                ptr.next = right
                right = right.next
            ptr = ptr.next
        ptr.next = left or right  # Remaining nodes
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ''' Divide and conquer based solution. '''
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(left, right)


def main():
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1, l2, l3]
    res = Solution().mergeKLists(lists)
    assert res.val == 1
    assert res.next.val == 1
    assert res.next.next.val == 2
    assert res.next.next.next.val == 3
    assert res.next.next.next.next.val == 4
    assert res.next.next.next.next.next.val == 4
    assert res.next.next.next.next.next.next.val == 5
    assert res.next.next.next.next.next.next.next.val == 6

    lists = []
    assert Solution().mergeKLists(lists) is None

    lists = [[]]
    assert Solution().mergeKLists(lists) == []


if __name__ == '__main__':
    main()
