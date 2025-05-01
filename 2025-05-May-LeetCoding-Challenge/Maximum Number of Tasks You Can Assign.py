from bisect import bisect_left


class Solution:
    def maxTaskAssign(
            self, tasks: list[int], workers: list[int], pills: int, strength: int
    ) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(mid: int) -> bool:
            available = workers[-mid:]  # strongest k workers
            used = 0
            # process from hardest among first k easiest tasks
            for task in reversed(tasks[:mid]):
                assigned = False
                # first try assigning without pills
                if available[-1] >= task:
                    available.pop()
                    assigned = True
                if not assigned and used < pills:
                    # try with pills
                    idx = bisect_left(available, task - strength)
                    if idx < len(available):
                        available.pop(idx)
                        assigned = True
                        used += 1
                if not assigned:
                    return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        while left <= right:
            # binary search for number of tasks possible
            mid = (left + right) // 2
            if can_assign(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right


def main():
    tasks = [3, 2, 1]
    workers = [0, 3, 3]
    pills = 1
    strength = 1
    assert Solution().maxTaskAssign(tasks, workers, pills, strength) == 3

    tasks = [5, 4]
    workers = [0, 0, 0]
    pills = 1
    strength = 5
    assert Solution().maxTaskAssign(tasks, workers, pills, strength) == 1

    tasks = [10, 15, 30]
    workers = [0, 10, 10, 10, 10]
    pills = 3
    strength = 10
    assert Solution().maxTaskAssign(tasks, workers, pills, strength) == 2


if __name__ == '__main__':
    main()
