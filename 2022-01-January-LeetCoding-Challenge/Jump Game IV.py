# -*- coding: utf-8 -*-
from collections import defaultdict, deque
import queue
from typing import List


class NotSolution:
    def minJumps(self, arr: List[int]) -> int:
        ''' Graph and BFS based solution with no optimization leads to TLE. '''
        n = len(arr)
        index_map = defaultdict(list)  # Map of number to its indices
        for index, num in enumerate(arr):
            index_map[num].append(index)
        # Graph node is index i and edges are i-1, i+1 and j
        # where arr[i] == arr[j]
        graph = defaultdict(set)
        for index, num in enumerate(arr):
            if index != 0:
                graph[index].add(index-1)
            if index != n-1:
                graph[index].add(index+1)
            graph[index].update(index_map.get(num))
            graph[index].remove(index)  # Remove self from neighbour list
        # Search shortest distance between 0 and n-1 node using BFS
        queue, visited = [[0]], set()
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = graph[node]
                for neighbour in neighbours:
                    queue.append(path + [neighbour])
                    if neighbour == n-1:
                        return len(path)  # Return length of shortest
                visited.add(node)
        return 0


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        ''' Graph and BFS based solution with optimization. '''
        n, d = len(arr), defaultdict(list)
        # Create index map
        for index, num in enumerate(arr):
            d[num].append(index)
        # Perform BFS
        queue, visited = deque([(0, 0)]), set()
        while queue:
            steps, index = queue.popleft()
            if index == n-1:
                return steps
            for neighbour in (index-1, index+1):
                if 0 <= neighbour < n and neighbour not in visited:
                    queue.append((steps+1, neighbour))
            # Optimize -> Process neighbours of i == j
            for neighbour in d[arr[index]]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((steps+1, neighbour))
            d[arr[index]] = list()
        return 0


def main():
    arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    assert Solution().minJumps(arr) == 3

    arr = [7]
    assert Solution().minJumps(arr) == 0


if __name__ == '__main__':
    main()
