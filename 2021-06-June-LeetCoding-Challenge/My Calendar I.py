# -*- coding: utf-8 -*-
from bisect import insort, bisect


class MyCalendar1:
    def __init__(self):
        self.intervals = list()

    def book(self, start: int, end: int) -> bool:
        for interval in self.intervals:
            if set(range(start, end)).intersection(range(interval[0],
                                                         interval[1])):
                return False
        self.intervals.append((start, end))
        return True


class MyCalendar2:
    def __init__(self):
        self.intervals = list()

    def book(self, start: int, end: int) -> bool:
        for interval in self.intervals:
            # Case 1: Start is in interval
            if start >= interval[0] and start < interval[1]:
                return False
            # Case 2: End is in interval
            if end > interval[0] and end < interval[1]:
                return False
            # Case 3: Range is superset of interval
            if start < interval[0] and end >= interval[1]:
                return False
        insort(self.intervals, (start, end))
        return True


class MyCalendar:
    def __init__(self):
        self.starts = list()
        self.ends = list()
        self.num = 0

    def __insert_interval(self, index, start, end):
        self.starts.insert(index, start)
        self.ends.insert(index, end)
        self.num += 1
        return True

    def book(self, start: int, end: int) -> bool:
        index = bisect(self.starts, start)  # Get start insert position

        # If insert position is at beginning
        if index == 0:
            # Check if end of range is lesser than first interval's start
            if not self.ends or self.ends and end <= self.starts[0]:
                return self.__insert_interval(index, start, end)
            else:
                return False

        # If insert position is at end
        if index == self.num:
            # Check is start of range is higher than last interval's end
            if start >= self.ends[-1]:
                return self.__insert_interval(index, start, end)
            return False

        # If insert position is in the middle
        # Check if start of range is higher than previous interval's end
        # Check if end of range is lesser than next interval's start
        if start >= self.ends[index-1] and end <= self.starts[index]:
            return self.__insert_interval(index, start, end)
        return False


if __name__ == '__main__':
    obj = MyCalendar()
    assert obj.book(10, 20)
    assert not obj.book(15, 25)
    assert obj.book(20, 30)

    obj = MyCalendar()
    assert obj.book(47, 50)
    assert obj.book(33, 41)
    assert not obj.book(39, 45)
    assert not obj.book(33, 42)
    assert obj.book(25, 32)
    assert not obj.book(26, 35)
    assert obj.book(19, 25)
    assert obj.book(3, 8)
    assert obj.book(8, 13)
    assert not obj.book(18, 27)

    obj = MyCalendar()
    assert obj.book(37, 50)
    assert not obj.book(33, 50)
    assert obj.book(4, 17)
    assert not obj.book(35, 48)
    assert not obj.book(8, 25)

    obj = MyCalendar()
    assert obj.book(20, 29)
    assert not obj.book(13, 22)
    assert obj.book(44, 50)
    assert obj.book(1, 7)
    assert not obj.book(2, 10)
    assert obj.book(14, 20)
    assert not obj.book(19, 25)
    assert obj.book(36, 42)
