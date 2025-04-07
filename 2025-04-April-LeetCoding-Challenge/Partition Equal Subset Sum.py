from functools import cache


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total & 1 != 0:
            return False
        else:
            total = total // 2

        @cache
        def dfs(index: int, target: int) -> bool:
            if target < 0:
                return False
            if target == 0:
                return True

            for i, num in enumerate(nums[index:], index):
                if dfs(i+1, target-num):
                    return True
            return False

        nums.sort(reverse=True)
        return dfs(0, total)


def main():
    nums = [1, 5, 11, 5]
    assert Solution().canPartition(nums) is True

    nums = [1, 2, 3, 5]
    assert Solution().canPartition(nums) is False


if __name__ == '__main__':
    main()
