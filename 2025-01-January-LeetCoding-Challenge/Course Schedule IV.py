from itertools import product
from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            is_prerequisite[u][v] = True

        for inter in range(numCourses):
            for u, v in product(range(numCourses), range(numCourses)):
                is_prerequisite[u][v] |= is_prerequisite[u][inter] and is_prerequisite[inter][v]

        return [is_prerequisite[u][v] for u, v in queries]


def main():
    numCourses = 2
    prerequisites = [[1, 0]]
    queries = [[0, 1], [1, 0]]
    assert Solution().checkIfPrerequisite(numCourses, prerequisites, queries) == [False, True]

    numCourses = 2
    prerequisites = []
    queries = [[1, 0], [0, 1]]
    assert Solution().checkIfPrerequisite(numCourses, prerequisites, queries) == [False, False]

    numCourses = 3
    prerequisites = [[1, 2], [1, 0], [2, 0]]
    queries = [[1, 0], [1, 2]]
    assert Solution().checkIfPrerequisite(numCourses, prerequisites, queries) == [True, True]


if __name__ == '__main__':
    main()
