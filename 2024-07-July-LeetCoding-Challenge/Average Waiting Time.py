from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        wait_time = 0
        for arrival, time in customers:
            current_time = max(current_time, arrival) + time
            wait_time += (current_time - arrival)
        return wait_time / len(customers)


def main():
    epsilon = 1e-5

    customers = [[1, 2], [2, 5], [4, 3]]
    assert abs(Solution().averageWaitingTime(customers) - 5.0) < epsilon

    customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
    assert abs(Solution().averageWaitingTime(customers) - 3.25) < epsilon


if __name__ == '__main__':
    main()
