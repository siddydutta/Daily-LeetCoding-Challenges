class Solution:
    def __init__(self):
        self.edges = []

    def __compute_distances(self, start: int) -> list[int]:
        distances = [-1] * len(self.edges)
        last_node = [(start, 0)]  # every node has at-most one outgoing edge
        visited = set()
        while last_node:
            node, distance = last_node.pop()
            if node in visited:
                continue
            distances[node] = distance
            visited.add(node)
            if self.edges[node] != -1:
                last_node.append((self.edges[node], distance + 1))
        return distances

    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        self.edges = edges
        distances1, distances2 = map(self.__compute_distances, (node1, node2))
        min_idx, max_min_dist = -1, float('inf')
        for idx, (d1, d2) in enumerate(zip(distances1, distances2)):
            if d1 == -1 or d2 == -1:
                continue
            curr_max = max(d1, d2)
            if curr_max < max_min_dist:
                min_idx = idx
                max_min_dist = curr_max
        return min_idx


def main():
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    assert Solution().closestMeetingNode(edges, node1, node2) == 2

    edges = [1, 2, -1]
    node1 = 0
    node2 = 2
    assert Solution().closestMeetingNode(edges, node1, node2) == 2


if __name__ == '__main__':
    main()
