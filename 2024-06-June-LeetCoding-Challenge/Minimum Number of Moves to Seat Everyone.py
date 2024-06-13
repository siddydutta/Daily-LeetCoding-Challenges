from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for seat, student in zip(seats, students):
            moves += abs(seat-student)
        return moves


def main():
    seats = [3, 1, 5]
    students = [2, 7, 4]
    assert Solution().minMovesToSeat(seats, students) == 4

    seats = [4, 1, 5, 9]
    students = [1, 3, 2, 6]
    assert Solution().minMovesToSeat(seats, students) == 7

    seats = [2, 2, 6, 6]
    students = [1, 3, 2, 6]
    assert Solution().minMovesToSeat(seats, students) == 4


if __name__ == '__main__':
    main()
