from math import gcd
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
            self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = head
        while prev.next is not None:
            node = ListNode(val=gcd(prev.val, prev.next.val), next=prev.next)
            prev.next = node
            prev = node.next
        return head


def main():
    head = ListNode(18)
    head.next = ListNode(6)
    head.next.next = ListNode(10)
    head.next.next.next = ListNode(3)
    result = Solution().insertGreatestCommonDivisors(head)
    assert result.val == 18
    assert result.next.val == 6
    assert result.next.next.val == 6
    assert result.next.next.next.val == 2
    assert result.next.next.next.next.val == 10
    assert result.next.next.next.next.next.val == 1
    assert result.next.next.next.next.next.next.val == 3
    assert result.next.next.next.next.next.next.next is None

    head = ListNode(7)
    result = Solution().insertGreatestCommonDivisors(head)
    assert result.val == 7
    assert result.next is None


if __name__ == '__main__':
    main()
