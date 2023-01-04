from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        rounds = 0
        for task, n in count.items():
            if n < 2:
                return -1
            rounds += (n+2) // 3
        return rounds


def main():
    tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    assert Solution().minimumRounds(tasks) == 4

    tasks = [2, 3, 3]
    assert Solution().minimumRounds(tasks) == -1


if __name__ == '__main__':
    main()
