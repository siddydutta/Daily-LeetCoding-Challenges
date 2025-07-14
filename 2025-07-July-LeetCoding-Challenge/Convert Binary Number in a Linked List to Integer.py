# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = 0
        while head is not None:
            binary *= 2
            binary += head.val
            head = head.next
        return binary


def main():
    head = ListNode(1, ListNode(0, ListNode(1)))
    assert Solution().getDecimalValue(head) == 5

    head = ListNode(0)
    assert Solution().getDecimalValue(head) == 0


if __name__ == '__main__':
    main()
