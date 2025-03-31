from itertools import pairwise


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        pair_sum = [w1 + w2 for w1, w2 in pairwise(weights)]
        pair_sum.sort()
        diff = 0
        for i in range(k - 1):
            diff += pair_sum[len(weights) - 2 - i] - pair_sum[i]
        return diff


def main():
    weights = [1, 3, 5, 1]
    k = 2
    assert Solution().putMarbles(weights, k) == 4

    weights = [1, 3]
    k = 2
    assert Solution().putMarbles(weights, k) == 0


if __name__ == '__main__':
    main()
