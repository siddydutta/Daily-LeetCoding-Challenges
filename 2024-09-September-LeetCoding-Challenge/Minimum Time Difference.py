from typing import List


class Time:
    TOTAL_MINS = 24 * 60

    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def get_minutes(self) -> int:
        return self.hour*60 + self.minute

    def __lt__(self, other: 'Time') -> bool:
        # first compare hour then minute
        return (self.hour, self.minute) < (other.hour, other.minute)

    def __sub__(self, other: 'Time') -> int:
        diff = abs(self.get_minutes() - other.get_minutes())
        return min(diff, self.TOTAL_MINS-diff)

    def __str__(self) -> str:
        return f'{self.hour:02}:{self.minute:02}'


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            hour, minute = list(map(int, time.split(':')))
            times.append(Time(hour, minute))
        times.sort()
        # handle wrap around case - last time to first time
        times.append(times[0])

        min_diff = Time.TOTAL_MINS
        for i in range(len(times)-1):
            min_diff = min(min_diff, times[i+1]-times[i])
        return min_diff


def main():
    timePoints = ['23:59', '00:00']
    assert Solution().findMinDifference(timePoints) == 1

    timePoints = ['00:00', '23:59', '00:00']
    assert Solution().findMinDifference(timePoints) == 0


if __name__ == '__main__':
    main()
