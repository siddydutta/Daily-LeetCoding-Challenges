from itertools import combinations
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_freq = dict()
        count = 0
        for a, b in combinations(nums, 2):
            product = a * b
            if product in product_freq:
                count += 8 * product_freq[product]
                product_freq[product] += 1
            else:
                product_freq[product] = 1
        return count


def main():
    nums = [2, 3, 4, 6]
    assert Solution().tupleSameProduct(nums) == 8

    nums = [1, 2, 4, 5, 10]
    assert Solution().tupleSameProduct(nums) == 16


if __name__ == '__main__':
    main()
