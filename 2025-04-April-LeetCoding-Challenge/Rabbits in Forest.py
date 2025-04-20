from collections import Counter
import math


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        frequencies = Counter(answers)
        total = 0
        for answer, count in frequencies.items():
            size = answer + 1
            groups = math.ceil(count / size)
            total += groups * size
        return total


def main():
    answers = [1, 1, 2]
    assert Solution().numRabbits(answers) == 5

    answers = [10, 10, 10]
    assert Solution().numRabbits(answers) == 11


if __name__ == '__main__':
    main()
