from bisect import bisect


class MyCalendar:
    def __init__(self):
        self.starts = list()
        self.ends = list()

    def book(self, start: int, end: int) -> bool:
        index = bisect(self.starts, start)
        if index == 0:
            if not self.ends or self.ends and end <= self.starts[0]:
                self.starts.insert(index, start)
                self.ends.insert(index, end)
                return True
        elif index == len(self.starts):
            if start >= self.ends[-1]:
                self.starts.append(start)
                self.ends.append(end)
                return True
        elif start >= self.ends[index-1] and end <= self.starts[index]:
            self.starts.insert(index, start)
            self.ends.insert(index, end)
            return True
        return False


def main():
    my_calendar = MyCalendar()
    assert my_calendar.book(10, 20) is True
    assert my_calendar.book(15, 25) is False
    assert my_calendar.book(20, 30) is True


if __name__ == '__main__':
    main()
