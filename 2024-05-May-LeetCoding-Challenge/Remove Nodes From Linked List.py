from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # reverse linked list
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # filter
        dummy = ListNode()
        prev, curr = dummy, prev
        while curr:
            if curr.val >= prev.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None
        # reverse linked list
        prev, curr = None, dummy.next
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


def main():
    head = ListNode(5)
    head.next = ListNode(2)
    head.next.next = ListNode(13)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(8)
    head = Solution().removeNodes(head)
    assert head.val == 13
    assert head.next.val == 8
    assert head.next.next is None

    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(1)
    head = Solution().removeNodes(head)
    assert head.val == 1
    assert head.next.val == 1
    assert head.next.next.val == 1
    assert head.next.next.next.val == 1
    assert head.next.next.next.next is None


if __name__ == '__main__':
    main()
