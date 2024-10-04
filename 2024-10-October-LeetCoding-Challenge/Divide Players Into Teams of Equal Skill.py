from collections import Counter
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target = sum(skill) // (len(skill)//2)
        freqs = Counter(skill)
        result = 0
        for i in range(len(skill)):
            skill1, skill2 = skill[i], target-skill[i]
            if freqs[skill1] == 0:
                # every pair is matched twice
                continue
            if freqs[skill2] == 0:
                return -1
            freqs[skill1] -= 1
            freqs[skill2] -= 1
            result += (skill1 * skill2)
        return result


def main():
    skill = [3, 2, 5, 1, 3, 4]
    assert Solution().dividePlayers(skill) == 22

    skill = [3, 4]
    assert Solution().dividePlayers(skill) == 12

    skill = [1, 1, 2, 3]
    assert Solution().dividePlayers(skill) == -1


if __name__ == '__main__':
    main()
