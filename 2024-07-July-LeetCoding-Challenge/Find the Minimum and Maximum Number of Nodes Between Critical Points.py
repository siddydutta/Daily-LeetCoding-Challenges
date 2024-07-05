from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        first_cp, last_cp = 0, 0
        prev_idx, curr_idx = 0, 1
        min_dist = 10**5 + 1

        while head.next.next is not None:
            if (head.val < head.next.val and head.next.val > head.next.next.val) or (  # noqa: E501
                head.val > head.next.val and head.next.val < head.next.next.val
            ):
                if not first_cp:
                    first_cp = curr_idx
                last_cp = curr_idx
                if prev_idx:
                    min_dist = min(min_dist, curr_idx-prev_idx)
                prev_idx = curr_idx
            curr_idx += 1
            head = head.next

        max_dist = last_cp - first_cp
        return [min_dist, max_dist] if max_dist else [-1, -1]


def main():
    head = ListNode(3)
    head.next = ListNode(1)
    assert Solution().nodesBetweenCriticalPoints(head) == [-1, -1]

    head = ListNode(5)
    head.next = ListNode(3)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(1)
    head.next.next.next.next.next.next = ListNode(2)
    assert Solution().nodesBetweenCriticalPoints(head) == [1, 3]

    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next.next.next = ListNode(7)
    assert Solution().nodesBetweenCriticalPoints(head) == [3, 3]
