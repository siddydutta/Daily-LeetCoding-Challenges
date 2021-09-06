# -*- coding: utf-8 -*-
from typing import List


class ListNode:
    '''
    Definition for singly-linked list.
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode,
                       left: int, right: int) -> ListNode:
        # Base case scenario
        if left == right:
            return head

        node = ptr = ListNode()  # Dummy node before actual linked list
        node.next = head

        # First traverse to node before reversing starts
        for _ in range(1, left):
            ptr = ptr.next

        # Start reversing from next node using three pointer approach
        current_node = ptr.next
        while left < right:
            temp_node = current_node.next
            current_node.next = temp_node.next
            temp_node.next = ptr.next
            ptr.next = temp_node
            left += 1

        return node.next


def create_linked_list(elements: List[int]) -> ListNode:
    head = ListNode()
    head_copy = head
    while elements:
        new_node = ListNode(elements.pop(0))
        head.next = new_node
        head = head.next
    return head_copy.next


def get_linked_list(head: ListNode) -> List[int]:
    elements = list()
    while head:
        elements.append(head.val)
        head = head.next
    return elements


def main():
    obj = Solution()
    ll = [1, 2, 3, 4, 5]
    head = create_linked_list(ll)
    left = 2
    right = 4
    result_head = obj.reverseBetween(head, left, right)
    assert get_linked_list(result_head) == [1, 4, 3, 2, 5]

    obj = Solution()
    ll = [5]
    head = create_linked_list(ll)
    left = 1
    right = 1
    result_head = obj.reverseBetween(head, left, right)
    assert get_linked_list(result_head) == [5]

    obj = Solution()
    ll = [3, 5]
    head = create_linked_list(ll)
    left = 1
    right = 2
    result_head = obj.reverseBetween(head, left, right)
    assert get_linked_list(result_head) == [5, 3]


if __name__ == '__main__':
    main()
