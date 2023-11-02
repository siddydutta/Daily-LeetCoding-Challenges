from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequency = defaultdict(int)
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            frequency[node.val] += 1
            nodes.extend(filter(None, [node.left, node.right]))

        max_freq = max(frequency.values())
        return [k for k, v in frequency.items() if v == max_freq]


def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    assert Solution().findMode(root) == [2]

    root = TreeNode(0)
    assert Solution().findMode(root) == [0]


if __name__ == '__main__':
    main()
