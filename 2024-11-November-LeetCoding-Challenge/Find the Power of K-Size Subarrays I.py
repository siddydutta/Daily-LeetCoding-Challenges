from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = 1
        left = 0
        for right in range(len(nums)):
            if right > 0 and nums[right-1]+1 == nums[right]:
                count += 1
            if right-left+1 > k:
                if nums[left+1] == nums[left]+1:
                    count -= 1
                left += 1
            if right-left+1 == k:
                result.append(nums[right] if count == k else -1)
        return result


def main():
    nums = [1, 2, 3, 4, 3, 2, 5]
    k = 3
    assert Solution().resultsArray(nums, k) == [3, 4, -1, -1, -1]

    nums = [2, 2, 2, 2, 2]
    k = 4
    assert Solution().resultsArray(nums, k) == [-1, -1]

    nums = [3, 2, 3, 2, 3, 2]
    k = 2
    assert Solution().resultsArray(nums, k) == [-1, 3, -1, 3, -1]


if __name__ == '__main__':
    main()
