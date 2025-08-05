class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        unplaced = 0
        for quantity in fruits:
            for idx, capacity in enumerate(baskets):
                if quantity <= capacity:
                    baskets[idx] = 0
                    break
            else:
                unplaced += 1
        return unplaced


def main():
    fruits = [4, 2, 5]
    baskets = [3, 5, 4]
    assert Solution().numOfUnplacedFruits(fruits, baskets) == 1

    fruits = [3, 6, 1]
    baskets = [6, 4, 7]
    assert Solution().numOfUnplacedFruits(fruits, baskets) == 0


if __name__ == '__main__':
    main()
