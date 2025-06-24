class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        result = []
        right = 0
        for i in range(n):
            if nums[i] != key:
                continue
            left = max(right, i - k)
            right = min(i + k, n - 1) + 1
            for j in range(left, right):
                result.append(j)
        return result


def main():
    nums = [3, 4, 9, 1, 3, 9, 5]
    key = 9
    k = 1
    assert Solution().findKDistantIndices(nums, key, k) == [1, 2, 3, 4, 5, 6]

    nums = [2, 2, 2, 2, 2]
    key = 2
    k = 2
    assert Solution().findKDistantIndices(nums, key, k) == [0, 1, 2, 3, 4]


if __name__ == '__main__':
    main()
