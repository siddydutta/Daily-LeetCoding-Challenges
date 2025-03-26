from itertools import product


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        array = [grid[x][y] for x, y in product(range(m), range(n))]
        array.sort()

        target = array[(m*n)//2]
        cost1, cost2 = 0, 0
        flag1, flag2 = True, True

        for num in array:
            diff = abs(num - target)
            if diff % x != 0:
                flag1 = False
                break
            cost1 += diff // x

        if m*n % 2 == 0:
            target = array[((m*n)//2)-1]
            for num in array:
                diff = abs(num-target)
                if diff % x != 0:
                    flag2 = False
                    break
                cost2 += diff // x

        if m*n % 2 == 0:
            if flag1 and flag2:
                return min(cost1, cost2)
            elif flag1 and not flag2:
                return cost1
            elif flag2 and not flag1:
                return cost2
        else:
            if flag1:
                return cost1
        return -1


def main():
    grid = [[2, 4],
            [6, 8]]
    x = 2
    assert Solution().minOperations(grid, x) == 4

    grid = [[1, 5],
            [2, 3]]
    x = 1
    assert Solution().minOperations(grid, x) == 5

    grid = [[1, 2],
            [3, 4]]
    x = 2
    assert Solution().minOperations(grid, x) == -1


if __name__ == '__main__':
    main()
