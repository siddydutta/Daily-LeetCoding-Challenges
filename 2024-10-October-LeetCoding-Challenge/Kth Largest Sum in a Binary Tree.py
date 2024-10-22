from collections import deque
from heapq import heappop, heappush
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        queue = deque([root])
        while queue:
            level_sum = 0
            next_level = []
            while queue:
                node = queue.popleft()
                level_sum += node.val
                next_level.extend(filter(None, (node.left, node.right)))
            heappush(heap, level_sum)
            if len(heap) > k:
                heappop(heap)
            queue = deque(next_level)
        return heap[0] if len(heap) == k else -1


def main():
    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(6)
    k = 2
    assert Solution().kthLargestLevelSum(root, k) == 13

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    k = 1
    assert Solution().kthLargestLevelSum(root, k) == 3


if __name__ == '__main__':
    main()
