# -*- coding: utf-8 -*-
from typing import List, Optional


class ListNode:
    ''' Definition for singly-linked list. '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode],
                         k: int) -> List[Optional[ListNode]]:
        # Find linkedlist length
        node = head
        length = 0
        while node:
            node = node.next
            length += 1

        # Compute number of elements per part and extra parts required
        n_elements = length // k
        extra_parts = length % k

        node = head
        result = list()
        for _ in range(k):
            if node is None:
                result.append(None)
                continue
            new_head = None
            ptr = new_head
            # Create new linkedlist with elements for part
            for i in range(n_elements):
                new_node = ListNode()
                new_node.val = node.val
                if ptr is None:
                    new_head = new_node
                    ptr = new_node
                else:
                    ptr.next = new_node
                    ptr = ptr.next
                node = node.next

            # Add extra element for first n%k parts
            if extra_parts > 0:
                new_node = ListNode()
                new_node.val = node.val
                if ptr is None:
                    new_head = new_node
                    ptr = new_node
                else:
                    ptr.next = new_node
                node = node.next
                extra_parts -= 1

            result.append(new_head)

        return result


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    k = 5
    result = Solution().splitListToParts(head, k)
    assert result[0].val == 1
    assert result[1].val == 2
    assert result[2].val == 3
    assert not result[3]
    assert not result[4]


if __name__ == '__main__':
    main()
