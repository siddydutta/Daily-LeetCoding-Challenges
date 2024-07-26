from typing import List


class Solution:
    def __merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.__merge(left, right)


def main():
    nums = [5, 2, 3, 1]
    assert Solution().sortArray(nums) == [1, 2, 3, 5]

    nums = [5, 1, 1, 2, 0, 0]
    assert Solution().sortArray(nums) == [0, 0, 1, 1, 2, 5]


if __name__ == '__main__':
    main()
