from itertools import combinations


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        count = 0
        for i, j in combinations(range(len(nums)), 2):
            count += ((nums[i] == nums[j]) and ((i * j) % k == 0))
        return count


def main():
    nums = [3, 1, 2, 2, 2, 1, 3]
    k = 2
    assert Solution().countPairs(nums, k) == 4

    nums = [1, 2, 3, 4]
    k = 1
    assert Solution().countPairs(nums, k) == 0


if __name__ == '__main__':
    main()
