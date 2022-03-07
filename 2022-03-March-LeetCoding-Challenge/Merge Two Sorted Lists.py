# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''' Solution based on merge-sort's merging logic. '''
        # Edge cases
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result, head = None, None
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                newNode = ListNode(l1.val, None)
                if head is None:
                    head = newNode
                    result = head
                else:
                    head.next = newNode
                    head = head.next
                l1 = l1.next
            else:
                newNode = ListNode(l2.val, None)
                if head is None:
                    head = newNode
                    result = head
                else:
                    head.next = newNode
                    head = head.next
                l2 = l2.next

        while l1 is not None:
            newNode = ListNode(l1.val, None)
            head.next = newNode
            head = head.next
            l1 = l1.next

        while l2 is not None:
            newNode = ListNode(l2.val, None)
            head.next = newNode
            head = head.next
            l2 = l2.next

        return result


def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    result = Solution().mergeTwoLists(list1, list2)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 4
    assert result.next.next.next.next.next.val == 4

    list1 = None
    list2 = None
    assert not Solution().mergeTwoLists(list1, list2)

    list1 = None
    list2 = ListNode(0)
    result = Solution().mergeTwoLists(list1, list2)
    assert result.val == 0
    assert not result.next


if __name__ == '__main__':
    main()
