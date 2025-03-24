class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        last, count = 0, 0
        for start, end in meetings:
            if last < start:
                count += start - last - 1
            last = max(last, end)
        count += days - last
        return count


def main():
    days = 10
    meetings = [[5, 7], [1, 3], [9, 10]]
    assert Solution().countDays(days, meetings) == 2

    days = 5
    meetings = [[2, 4], [1, 3]]
    assert Solution().countDays(days, meetings) == 1

    days = 6
    meetings = [[1, 6]]
    assert Solution().countDays(days, meetings) == 0


if __name__ == '__main__':
    main()
