from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for h, n in sorted(zip(heights, names), reverse=True)]


def main():
    names = ['Mary', 'John', 'Emma']
    heights = [180, 165, 170]
    assert Solution().sortPeople(names, heights) == ['Mary', 'Emma', 'John']

    names = ['Alice', 'Bob', 'Bob']
    heights = [155, 185, 150]
    assert Solution().sortPeople(names, heights) == ['Bob', 'Alice', 'Bob']


if __name__ == '__main__':
    main()
