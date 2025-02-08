from heapq import heappush, heappop
from collections import defaultdict


class NumberContainers:
    def __init__(self):
        self.idx_num_map = defaultdict(int)
        self.num_idxs_map = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idx_num_map[index] = number
        heappush(self.num_idxs_map[number], index)

    def find(self, number: int) -> int:
        while self.num_idxs_map[number]:
            smallest_idx = self.num_idxs_map[number][0]
            if self.idx_num_map[smallest_idx] == number:
                return smallest_idx
            heappop(self.num_idxs_map[number])
        return -1


def main():
    nc = NumberContainers()
    assert nc.find(10) == -1
    nc.change(2, 10)
    nc.change(1, 10)
    nc.change(3, 10)
    nc.change(5, 10)
    assert nc.find(10) == 1
    nc.change(1, 20)
    assert nc.find(10) == 2


if __name__ == '__main__':
    main()
