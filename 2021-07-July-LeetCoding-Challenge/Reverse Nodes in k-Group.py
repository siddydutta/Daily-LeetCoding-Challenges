# -*- coding: utf-8 -*-
class ListNode:
    ''' Definition for singly-linked list. '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    Makes use of a previous pointer to reverse k elements at a time.
    Time Complexity: O(n)
    '''
    def __nodesCount(self, head: ListNode) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = self.__nodesCount(head)
        dummy = ListNode()  # Dummy node to serve as pre before linked list
        dummy.next = head
        previous = dummy  # Pre points to the node before k-group to reverse

        while n >= k:
            current = previous.next  # Current points to the node to reverse
            follow = current.next
            for _ in range(k-1):  # A k-group undergoes k-1 reverse operations
                current.next = follow.next
                follow.next = previous.next
                previous.next = follow
                follow = current.next
            previous = current  # Update previous for next k-group
            n -= k

        return dummy.next


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    k = 2
    # 1->2 --> 2->1
    result = Solution().reverseKGroup(head, k)
    assert result.val == 2
    assert result.next.val == 1

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2
    # 1->2->3->4->5 --> 2->1->4->3->5
    result = Solution().reverseKGroup(head, k)
    assert result.val == 2
    assert result.next.val == 1
    assert result.next.next.val == 4
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 5


if __name__ == '__main__':
    main()
