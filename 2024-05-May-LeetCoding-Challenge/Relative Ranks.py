from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        elements = sorted([(s, i) for i, s in enumerate(score)])
        for medal in ('Gold Medal', 'Silver Medal', 'Bronze Medal'):
            if elements:
                score[elements[-1][1]] = medal
                elements.pop()
        for i, (_, idx) in enumerate(reversed(elements), start=4):
            score[idx] = str(i)
        return score


def main():
    score = [5, 4, 3, 2, 1]
    assert Solution().findRelativeRanks(score) == ['Gold Medal',
                                                   'Silver Medal',
                                                   'Bronze Medal',
                                                   '4',
                                                   '5']

    score = [10, 3, 8, 9, 4]
    assert Solution().findRelativeRanks(score) == ['Gold Medal',
                                                   '5',
                                                   'Bronze Medal',
                                                   'Silver Medal',
                                                   '4']


if __name__ == '__main__':
    main()
