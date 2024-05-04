from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        boats = 0
        while left <= right:
            person = people[right]
            if person + people[left] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats


def main():
    people = [1, 2]
    limit = 3
    assert Solution().numRescueBoats(people, limit) == 1

    people = [3, 2, 2, 1]
    limit = 3
    assert Solution().numRescueBoats(people, limit) == 3

    people = [3, 5, 3, 4]
    limit = 5
    assert Solution().numRescueBoats(people, limit) == 4


if __name__ == '__main__':
    main()
