from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        empty_chairs = list(range(len(times)))
        activity = []
        for person, (start, end) in enumerate(times):
            activity.append((start, True, person))
            activity.append((end, False, person))
        heapify(activity)

        seating = [-1] * len(times)
        while activity:
            _, is_start, person = heappop(activity)
            if is_start:
                if person == targetFriend:
                    return empty_chairs[0]
                seating[person] = heappop(empty_chairs)
            else:
                heappush(empty_chairs, seating[person])


def main():
    times = [[1, 4], [2, 3], [4, 6]]
    targetFriend = 1
    assert Solution().smallestChair(times, targetFriend) == 1

    times = [[3, 10], [1, 5], [2, 6]]
    targetFriend = 0
    assert Solution().smallestChair(times, targetFriend) == 2


if __name__ == '__main__':
    main()
