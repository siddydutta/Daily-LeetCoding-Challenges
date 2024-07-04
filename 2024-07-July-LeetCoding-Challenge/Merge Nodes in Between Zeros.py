from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        curr_sum = 0

        while curr is not None:
            if curr.val == 0:
                prev = prev.next
                prev.val = curr_sum
                curr_sum = 0
            else:
                curr_sum += curr.val
            curr = curr.next

        prev.next = None
        return head.next


def main():
    head = ListNode(0)
    head.next = ListNode(3)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(0)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next.next = ListNode(0)
    result = Solution().mergeNodes(head)
    assert result.val == 4
    assert result.next.val == 11
    assert result.next.next is None

    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(0)
    head.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next.next = ListNode(0)
    result = Solution().mergeNodes(head)
    assert result.val == 1
    assert result.next.val == 3
    assert result.next.next.val == 4
    assert result.next.next.next is None


if __name__ == '__main__':
    main()
