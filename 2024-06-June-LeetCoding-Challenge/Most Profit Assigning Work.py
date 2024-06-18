from typing import List


class Job:
    def __init__(self, diff: int, profit: int):
        self.diff = diff
        self.profit = profit


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        worker.sort(reverse=True)
        jobs = [Job(diff, profit) for diff, profit in zip(difficulty, profit)]
        jobs.sort(key=lambda j: j.profit)

        total_profit = 0
        for w in worker:
            while jobs and w < jobs[-1].diff:
                # remove all jobs with more difficulty
                jobs.pop()

            if jobs:
                total_profit += jobs[-1].profit
            else:
                # if curr worker can't do any jobs
                # subsequent workers won't
                break
        return total_profit


def main():
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    assert Solution().maxProfitAssignment(difficulty, profit, worker) == 100

    difficulty = [85, 47, 57]
    profit = [24, 66, 99]
    worker = [40, 25, 25]
    assert Solution().maxProfitAssignment(difficulty, profit, worker) == 0


if __name__ == '__main__':
    main()
