from typing import Generator, List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        def dfs(node: Optional[Node]) -> Generator[int, int, int]:
            if node is not None:
                for child in node.children:
                    yield from dfs(child)
                yield node.val
        return list(dfs(root))


def main():
    root = Node(1)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    assert Solution().postorder(root) == [5, 6, 3, 2, 4, 1]

    root = Node(1)
    root.children = [Node(2), Node(3), Node(4), Node(5)]
    root.children[1].children = [Node(6), Node(7)]
    root.children[2].children = [Node(8)]
    root.children[3].children = [Node(9), Node(10)]
    root.children[1].children[1].children = [Node(11)]
    root.children[2].children[0].children = [Node(12)]
    root.children[3].children[0].children = [Node(13)]
    root.children[1].children[1].children[0].children = [Node(14)]
    nodes = [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
    assert Solution().postorder(root) == nodes


if __name__ == '__main__':
    main()
