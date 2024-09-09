from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
            self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(next=head)
        ptr = dummy
        while ptr.next is not None:
            if ptr.next.val in nums:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next


def main():
    nums = [1, 2, 3]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    result = Solution().modifiedList(nums, head)
    assert result.val == 4
    assert result.next.val == 5
    assert result.next.next is None

    nums = [1]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    head.next.next.next.next.next = ListNode(2)
    result = Solution().modifiedList(nums, head)
    assert result.val == 2
    assert result.next.val == 2
    assert result.next.next.val == 2
    assert result.next.next.next is None

    nums = [5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    result = Solution().modifiedList(nums, head)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next is None


if __name__ == '__main__':
    main()
