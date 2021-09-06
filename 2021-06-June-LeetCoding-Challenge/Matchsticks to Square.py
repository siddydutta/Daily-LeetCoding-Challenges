# -*- coding: utf-8 -*-
from typing import List


class NotSolution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        def dfs(index, top, bottom, left, right, arr, x) -> bool:
            if top > x or bottom > x or left > x or right > x:
                return False
            if index == len(arr):
                return top == bottom and bottom == left and left == right

            return dfs(index+1, top+arr[index], bottom, left, right, arr, x) \
                or dfs(index+1, top, bottom+arr[index], left, right, arr, x) \
                or dfs(index+1, top, bottom, left+arr[index], right, arr, x) \
                or dfs(index+1, top, bottom, left, right+arr[index], arr, x)

        return dfs(0, 0, 0, 0, 0, matchsticks, total//4)


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        res = set()

        def dfs(i, arr, path, res, side):
            if len(res) == len(arr):
                return
            if path[1] == side:
                res.update(path[0])
                return
            if path[1] > side:
                return
            for x in range(i, len(arr)):
                if len(res) == len(arr):
                    break
                dfs(x+1, arr, [path[0]+[x], path[1]+arr[x]], res, side)

        dfs(0, matchsticks, [[], 0], res, total//4)
        return len(res) == len(matchsticks)


if __name__ == '__main__':
    obj = Solution()
    matchsticks = [1, 1, 2, 2, 2]
    assert obj.makesquare(matchsticks)

    matchsticks = [3, 3, 3, 3, 4]
    assert not obj.makesquare(matchsticks)
