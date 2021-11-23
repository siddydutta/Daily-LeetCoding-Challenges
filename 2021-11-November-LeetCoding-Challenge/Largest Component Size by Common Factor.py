# -*- coding: utf-8 -*-
from collections import Counter, defaultdict
from math import sqrt
from typing import List, Set


class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        xp, yp = self.find(x), self.find(y)
        self.parent[xp] = yp


class Solution:
    def __primes_set(self, n: int) -> Set:
        ''' Returns a generated set of primes for n. '''
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return self.__primes_set(n // i) | set([i])
        return set([n])

    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UF(len(nums))
        primes = defaultdict(list)

        for idx, num in enumerate(nums):
            for p in self.__primes_set(num):
                primes[p].append(idx)

        for indices in primes.values():
            for i in range(len(indices)-1):
                uf.union(indices[i], indices[i+1])

        return max(Counter([uf.find(i) for i in range(len(nums))]).values())


def main():
    nums = [4, 6, 15, 35]
    assert Solution().largestComponentSize(nums) == 4

    nums = [20, 50, 9, 63]
    assert Solution().largestComponentSize(nums) == 2

    nums = [2, 3, 6, 7, 4, 12, 21, 39]
    assert Solution().largestComponentSize(nums) == 8


if __name__ == '__main__':
    main()
