from itertools import accumulate
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_travel = list(accumulate(travel))
        m_count, p_count, g_count = 0, 0, 0
        m_last, p_last, g_last = 0, 0, 0
        for index, house in enumerate(garbage):
            for unit in house:
                if unit == 'M':
                    m_count += 1
                    m_last = index
                elif unit == 'P':
                    p_count += 1
                    p_last = index
                elif unit == 'G':
                    g_count += 1
                    g_last = index

        mins = m_count + p_count + g_count
        if m_last:
            mins += total_travel[m_last-1]
        if p_last:
            mins += total_travel[p_last-1]
        if g_last:
            mins += total_travel[g_last-1]
        return mins


def main():
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]
    assert Solution().garbageCollection(garbage, travel) == 21

    garbage = ["MMM", "PGM", "GP"]
    travel = [3, 10]
    assert Solution().garbageCollection(garbage, travel) == 37

    garbage = ["G", "M"]
    travel = [1]
    assert Solution().garbageCollection(garbage, travel) == 3


if __name__ == '__main__':
    main()
