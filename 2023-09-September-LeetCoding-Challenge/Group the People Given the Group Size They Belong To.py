from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = defaultdict(list)
        for person, group_no in enumerate(groupSizes):
            group[group_no].append(person)
        groups = []
        for size, people in group.items():
            while people:
                groups.append(people[:size])
                people = people[size:]
        return groups


def main():
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    assert Solution().groupThePeople(groupSizes) == [[0, 1, 2], [3, 4, 6], [5]]

    groupSizes = [2, 1, 3, 3, 3, 2]
    assert Solution().groupThePeople(groupSizes) == [[0, 5], [1], [2, 3, 4]]


if __name__ == '__main__':
    main()
