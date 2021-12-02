# -*- coding: utf-8 -*-
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' Time Complexity: O(n)    Space Complexity: O(1) '''
        if head is None or head.next is None:
            return head  # Edge cases

        odd_ptr = head
        even_ptr = head.next
        dummy = even_ptr  # To maintain start of even pointer

        while even_ptr is not None and even_ptr.next is not None:
            odd_ptr.next = odd_ptr.next.next  # Join next odd
            odd_ptr = odd_ptr.next  # Move to next odd
            even_ptr.next = even_ptr.next.next  # Join next even
            even_ptr = even_ptr.next  # Move to next even
        odd_ptr.next = dummy  # Join the end of odd and start of even

        return head


def create_linked_list(vals: List) -> ListNode:
    head = None
    dummy = head
    for val in vals:
        if head is None:
            head = ListNode(val)
            dummy = head
        else:
            node = ListNode(val)
            head.next = node
            head = head.next
    return dummy


def verify_linked_list(head: ListNode, expected_vals: List) -> bool:
    idx = 0
    while head:
        try:
            if head.val != expected_vals[idx]:
                return False
            idx += 1
            head = head.next
        except IndexError:
            return False
    return True


def main():
    vals = [1, 2, 3, 4, 5]
    head = create_linked_list(vals)
    result = Solution().oddEvenList(head)
    expected_vals = [1, 3, 5, 2, 4]
    assert verify_linked_list(result, expected_vals)

    vals = [2, 1, 3, 5, 6, 4, 7]
    head = create_linked_list(vals)
    result = Solution().oddEvenList(head)
    expected_vals = [2, 3, 6, 7, 1, 5, 4]
    assert verify_linked_list(result, expected_vals)


if __name__ == '__main__':
    main()
