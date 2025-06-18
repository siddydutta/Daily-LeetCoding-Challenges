class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            result.append(nums[i: i + 3])
        return result


def main():
    nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
    k = 2
    assert Solution().divideArray(nums, k) == [[1, 1, 3], [3, 4, 5], [7, 8, 9]]

    nums = [1, 3, 3, 2, 7, 3]
    k = 3
    assert Solution().divideArray(nums, k) == []


if __name__ == '__main__':
    main()
