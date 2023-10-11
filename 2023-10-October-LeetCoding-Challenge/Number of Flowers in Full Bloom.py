from enum import Enum
from typing import List, Optional


class EventType(Enum):
    START = 0
    PERSON = 1
    END = 2


class Event:
    def __init__(self, time: int, type: EventType, idx: Optional[int]=None):
        self.time = time
        self.type = type
        self.idx = idx

    def __lt__(self, other) -> int:
        if self.time == other.time:
            return self.type.value < other.type.value
        return self.time < other.time


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = list()
        for idx, time in enumerate(people):
            events.append(Event(time, EventType.PERSON, idx))
        for start, end in flowers:
            events.append(Event(start, EventType.START))
            events.append(Event(end, EventType.END))
        events = sorted(events)

        n_flowers = [0] * len(people)
        flowers = 0
        for event in events:
            if event.type == EventType.START:
                flowers += 1
            elif event.type == EventType.END:
                flowers -= 1
            elif event.type == EventType.PERSON:
                n_flowers[event.idx] = flowers
        return n_flowers


def main():
    flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
    people = [2, 3, 7, 11]
    assert Solution().fullBloomFlowers(flowers, people) == [1, 2, 2, 2]

    flowers = [[1, 10], [3, 3]]
    people = [3, 3, 2]
    assert Solution().fullBloomFlowers(flowers, people) == [2, 2, 1]


if __name__ == '__main__':
    main()
