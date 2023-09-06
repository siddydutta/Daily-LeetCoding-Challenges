from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        size, extra = divmod(length, k)

        result = []
        curr = head
        for _ in range(k):
            if curr is None:
                result.append(None)
                continue

            sub_head = None
            sub_curr = None
            for _ in range(size):
                if sub_curr is None:
                    sub_curr = curr
                    sub_head = sub_curr
                else:
                    sub_curr.next = curr
                    sub_curr = sub_curr.next
                curr = curr.next

            if extra > 0:
                if sub_curr is None:
                    sub_curr = curr
                    sub_head = sub_curr
                else:
                    sub_curr.next = curr
                    sub_curr = sub_curr.next
                curr = curr.next
                extra -= 1
            sub_curr.next = None

            result.append(sub_head)
        return result


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    k = 5
    res = Solution().splitListToParts(head, k)
    assert len(res) == k
    assert res[0].val == 1
    assert res[0].next is None
    assert res[1].val == 2
    assert res[1].next is None
    assert res[2].val == 3
    assert res[2].next is None
    assert res[3] is None
    assert res[4] is None

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    k = 3
    res = Solution().splitListToParts(head, k)
    assert len(res) == k
    assert res[0].val == 1
    assert res[0].next.val == 2
    assert res[0].next.next.val == 3
    assert res[0].next.next.next.val == 4
    assert res[0].next.next.next.next is None
    assert res[1].val == 5
    assert res[1].next.val == 6
    assert res[1].next.next.val == 7
    assert res[1].next.next.next is None
    assert res[2].val == 8
    assert res[2].next.val == 9
    assert res[2].next.next.val == 10
    assert res[2].next.next.next is None


if __name__ == '__main__':
    main()
