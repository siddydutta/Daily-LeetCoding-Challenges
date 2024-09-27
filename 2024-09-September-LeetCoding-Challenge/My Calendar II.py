from bisect import bisect_left, insort


class MyCalendarTwo:
    def __init__(self):
        self.meetings = []

    def book(self, start: int, end: int) -> bool:
        insort(self.meetings, (start, 1))
        insort(self.meetings, (end, -1))
        current = 0
        for _, n in self.meetings:
            current += n
            if current == 3:
                self.meetings.pop(bisect_left(self.meetings, (start, 1)))
                self.meetings.pop(bisect_left(self.meetings, (end, -1)))
                return False
        return True


def main():
    my_calender_two = MyCalendarTwo()
    assert my_calender_two.book(10, 20) is True
    assert my_calender_two.book(50, 60) is True
    assert my_calender_two.book(10, 40) is True
    assert my_calender_two.book(5, 15) is False
    assert my_calender_two.book(5, 10) is True
    assert my_calender_two.book(25, 55) is True


if __name__ == '__main__':
    main()
