from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
            self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        pre_index, post_index = 1, 0
        while stack:
            node = stack[-1]
            if node.val == postorder[post_index]:
                stack.pop()
                post_index += 1
            else:
                new_node = TreeNode(preorder[pre_index])
                pre_index += 1
                if node.left is None:
                    node.left = new_node
                else:
                    node.right = new_node
                stack.append(new_node)
        return root


def main():
    preorder = [1, 2, 4, 5, 3, 6, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    root = Solution().constructFromPrePost(preorder, postorder)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left.val == 4
    assert root.left.right.val == 5
    assert root.right.left.val == 6
    assert root.right.right.val == 7

    preorder = [1]
    postorder = [1]
    root = Solution().constructFromPrePost(preorder, postorder)
    assert root.val == 1


if __name__ == '__main__':
    main()
