import heapq


class SeatManager:

    def __init__(self, n: int):
        self.heap = list(range(1, n+1))

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


def main():
    seatManager = SeatManager(5)
    assert seatManager.reserve() == 1
    assert seatManager.reserve() == 2
    seatManager.unreserve(2)
    assert seatManager.reserve() == 2
    assert seatManager.reserve() == 3
    assert seatManager.reserve() == 4
    assert seatManager.reserve() == 5
    seatManager.unreserve(5)


if __name__ == '__main__':
    main()
