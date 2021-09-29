# -*- coding: utf-8 -*-
from typing import List, Optional


class ListNode:
    ''' Definition for singly-linked list. '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        return [head]


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next = ListNode(3)
    k = 5
    result = Solution().splitListToParts(head, k)
    assert result[0] == ListNode(1)
    assert result[1] == ListNode(2)
    assert result[2] == ListNode(3)
    assert result[3] == []
    assert result[4] == []


if __name__ == '__main__':
    main()
