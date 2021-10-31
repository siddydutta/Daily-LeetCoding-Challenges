# -*- coding: utf-8 -*-
class Node:
    ''' Definition for a Node. '''
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    ''' DFS based solution. '''
    def flatten(self, head: 'Node') -> 'Node':
        node = head  # Pointer
        while node:
            if not node.child:
                # No child present
                node = node.next
            else:
                # If child present
                kid = node.child
                while kid.next:
                    kid = kid.next
                # Link last child to next node
                kid.next = node.next
                if node.next:
                    node.next.prev = kid
                # Connect node to child and remove child pointer
                node.next = node.child
                node.child.prev = node
                node.child = None
        return head
