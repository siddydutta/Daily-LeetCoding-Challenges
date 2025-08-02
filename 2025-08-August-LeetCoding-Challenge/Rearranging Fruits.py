class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        freq = dict()
        min_fruit = float('inf')

        for fruit in basket1:
            freq[fruit] = freq.get(fruit, 0) + 1
            min_fruit = min(min_fruit, fruit)
        for fruit in basket2:
            freq[fruit] = freq.get(fruit, 0) - 1
            min_fruit = min(min_fruit, fruit)

        swap = []
        for fruit, count in freq.items():
            if count & 1 != 0:
                return -1
            swap.extend([fruit] * (abs(count) // 2))

        swap.sort()
        min_cost = 0
        for fruit in swap[:len(swap) // 2]:
            min_cost += min(2 * min_fruit, fruit)
        return min_cost


def main():
    basket1 = [4, 2, 2, 2]
    basket2 = [1, 4, 1, 2]
    assert Solution().minCost(basket1, basket2) == 1

    basket1 = [2, 3, 4, 1]
    basket2 = [3, 2, 5, 1]
    assert Solution().minCost(basket1, basket2) == -1


if __name__ == '__main__':
    main()
