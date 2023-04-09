# -*- coding: utf-8 -*-


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        adj = {node: Node(node.val)}
        self.dfs(node, adj)
        return adj[node]

    def dfs(self, node, adj):
        for neighbour in node.neighbors:
            if neighbour not in adj:
                adj[neighbour] = Node(neighbour.val)
                self.dfs(neighbour, adj)
            adj[node].neighbors.append(adj[neighbour])


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    res = Solution().cloneGraph(node1)
    assert res.val == 1
    assert res.neighbors[0].val == 2
    assert res.neighbors[1].val == 4
    assert res.neighbors[0].neighbors[0].val == 1
    assert res.neighbors[0].neighbors[1].val == 3
    assert res.neighbors[1].neighbors[0].val == 1
    assert res.neighbors[1].neighbors[1].val == 3

    node1 = Node(1)
    res = Solution().cloneGraph(node1)
    assert res.val == 1
    assert not res.neighbors

    res = Solution().cloneGraph(None)
    assert not res


if __name__ == '__main__':
    main()
