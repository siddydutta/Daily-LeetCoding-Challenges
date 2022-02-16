# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ''' Recursive solution. '''
        if not head or not head.next:
            return head  # Base Conition

        temp = head  # First Node
        head = head.next  # Second Node
        temp.next = head.next  # First node points to next pair
        head.next = temp  # Second node points to first node
        # Pairs are swapped. New second node points to next pair after swap
        temp.next = self.swapPairs(temp.next)  # Recursive call to next pair
        return head


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    res = Solution().swapPairs(head)
    assert res.val == 2
    assert res.next.val == 1
    assert res.next.next.val == 4
    assert res.next.next.next.val == 3

    head = None
    assert not Solution().swapPairs(head)

    head = ListNode(1)
    assert Solution().swapPairs(head).val == 1


if __name__ == '__main__':
    main()
