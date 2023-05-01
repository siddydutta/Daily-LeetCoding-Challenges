# -*- coding: utf-8 -*-
from math import inf
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary, min_salary = -inf, inf
        total = 0
        for s in salary:
            total += s
            min_salary = min(min_salary, s)
            max_salary = max(max_salary, s)
        return (total - min_salary - max_salary) / (len(salary)-2)


def main():
    salary = [4000, 3000, 1000, 2000]
    assert Solution().average(salary) == 2500.00000

    salary = [1000, 2000, 3000]
    assert Solution().average(salary) == 2000.00000


if __name__ == '__main__':
    main()
