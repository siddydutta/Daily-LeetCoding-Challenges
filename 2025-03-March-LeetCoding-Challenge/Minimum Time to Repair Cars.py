class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        left, right = 1, cars * cars * ranks[0]
        while left < right:
            mid = (left + right) // 2
            repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)
            if repaired >= cars:
                right = mid
            else:
                left = mid + 1
        return left


def main():
    ranks = [4, 2, 3, 1]
    cars = 10
    assert Solution().repairCars(ranks, cars) == 16

    ranks = [5, 1, 8]
    cars = 6
    assert Solution().repairCars(ranks, cars) == 16


if __name__ == '__main__':
    main()
