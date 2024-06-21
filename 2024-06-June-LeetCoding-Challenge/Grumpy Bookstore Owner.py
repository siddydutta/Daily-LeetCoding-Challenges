from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        init_happy = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                init_happy += customers[i]
                customers[i] = 0  # to prevent double count

        max_happy = init_happy
        curr_happy = init_happy
        for i in range(len(customers)):
            curr_happy += customers[i]
            if i >= minutes:
                # sliding window
                curr_happy -= customers[i - minutes]
            max_happy = max(max_happy, curr_happy)

        return max_happy


def main():
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3
    assert Solution().maxSatisfied(customers, grumpy, minutes) == 16

    customers = [1]
    grumpy = [0]
    minutes = 1
    assert Solution().maxSatisfied(customers, grumpy, minutes) == 1


if __name__ == '__main__':
    main()
