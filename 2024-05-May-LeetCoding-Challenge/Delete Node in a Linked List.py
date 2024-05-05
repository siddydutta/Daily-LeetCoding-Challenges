# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node is not None:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
            node = node.next


def main():
    node = ListNode(4)
    node.next = ListNode(5)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(9)
    Solution().deleteNode(node.next)
    assert node.val == 4
    assert node.next.val == 1
    assert node.next.next.val == 9
    assert node.next.next.next is None

    node = ListNode(4)
    node.next = ListNode(5)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(9)
    Solution().deleteNode(node.next.next)
    assert node.val == 4
    assert node.next.val == 5
    assert node.next.next.val == 9
    assert node.next.next.next is None


if __name__ == '__main__':
    main()
