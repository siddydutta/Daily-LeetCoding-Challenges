# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class NotSolution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ''' Less elegant solution involving creating two graphs. '''
        trusts_graph, trusted_by_graph = defaultdict(list), defaultdict(list)
        for u, v in trust:
            trusts_graph[u].append(v)  # People that trust somebody
            trusted_by_graph[v].append(u)  # People trusted by somebody

        for idx in range(1, n+1):
            # Judge should not trust somebody and be trusted by everybody else
            if idx not in trusts_graph and \
                    len(trusted_by_graph.get(idx, list())) == n-1:
                return idx
        return -1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ''' Graph node's degree count based solution. Time Complexity: O(n) '''
        trust_score = [0] * (n+1)
        for u, v in trust:
            trust_score[u] -= 1  # Trusting person has score reduced by 1
            trust_score[v] += 1  # Trusted person has score increased by 1

        for idx in range(1, len(trust_score)):
            if trust_score[idx] == n-1:
                return idx  # Judge is trusted by everyone except themself
        return -1


def main():
    n, trust = 2, [[1, 2]]
    assert Solution().findJudge(n, trust) == 2

    n, trust = 3, [[1, 3], [2, 3]]
    assert Solution().findJudge(n, trust) == 3

    n, trust = 3, [[1, 3], [2, 3], [3, 1]]
    assert Solution().findJudge(n, trust) == -1


if __name__ == '__main__':
    main()
