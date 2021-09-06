from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children  # List[Node]


class Solution:
    ''' Iterative solution using queue. '''
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Base case
        if not root:
            return list()

        queue = [[root]]  # Queue contains list of nodes level-wise
        result = list()

        while queue:
            level_nodes = queue.pop(0)  # All nodes at a particular level
            level_vals = list()
            children = list()  # Next level nodes
            for node in level_nodes:
                level_vals.append(node.val)
                if node.children:
                    children += node.children  # Extend children list
            if children:
                queue.append(children)
            result.append(level_vals)

        return result


def main():
    root = Node(1)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    assert Solution().levelOrder(root) == [[1], [3, 2, 4], [5, 6]]

    root = Node(1)
    root.children = [Node(2), Node(3), Node(4), Node(5)]
    root.children[1].children = [Node(6), Node(7)]
    root.children[2].children = [Node(8)]
    root.children[3].children = [Node(9), Node(10)]
    root.children[1].children[1].children = [Node(11)]
    root.children[2].children[0].children = [Node(12)]
    root.children[3].children[0].children = [Node(13)]
    root.children[1].children[1].children[0].children = [Node(14)]
    assert Solution().levelOrder(root) == [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10],
                                           [11, 12, 13], [14]]


if __name__ == '__main__':
    main()
