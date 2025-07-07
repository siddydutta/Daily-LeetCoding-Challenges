from heapq import heappop, heappush


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        n = len(events)
        events.sort(key=lambda e: (e[0], e[1]))
        heap = []  # heap to store end times
        idx, count = 0, 0
        for day in range(1, 100_001):
            # remove events that are over
            while heap and heap[0] < day:
                heappop(heap)
            # add current events to heap
            while idx < n and events[idx][0] == day:
                heappush(heap, events[idx][1])
                idx += 1
            # attend event
            if heap:
                heappop(heap)
                count += 1
        return count


def main():
    events = [[1, 2], [2, 3], [3, 4]]
    assert Solution().maxEvents(events) == 3

    events = [[1, 2], [2, 3], [3, 4], [1, 2]]
    assert Solution().maxEvents(events) == 4


if __name__ == '__main__':
    main()
