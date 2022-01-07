# -*- coding: utf-8 -*-
from random import choice, random
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    ''' Naive solution using extra space. '''
    def __init__(self, head: Optional[ListNode]):
        self.values = list()
        while head is not None:
            self.values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.values)


class Solution2:
    ''' Reservoir sampling. '''
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self):
        n, k = 1, 1
        node, res = self.head, self.head
        while node.next:
            n += 1
            node = node.next
            if random() < k/n:
                res = res.next
                k += 1
        return res.val


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    for obj in [Solution1(head), Solution2(head)]:
        assert obj.getRandom() in [1, 2, 3]
        assert obj.getRandom() in [1, 2, 3]
        assert obj.getRandom() in [1, 2, 3]
        assert obj.getRandom() in [1, 2, 3]


if __name__ == '__main__':
    main()
