class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lesser, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                lesser.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return lesser + equal + greater


def main():
    nums = [9, 12, 5, 10, 14, 3, 10]
    pivot = 10
    assert Solution().pivotArray(nums, pivot) == [9, 5, 3, 10, 10, 12, 14]

    nums = [-3, 4, 3, 2]
    pivot = 2
    assert Solution().pivotArray(nums, pivot) == [-3, 2, 4, 3]


if __name__ == '__main__':
    main()
