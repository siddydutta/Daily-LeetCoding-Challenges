from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m_or = 0
        for num in nums:
            m_or |= num

        def dfs(idx: int = 0, curr_or: int = 0) -> None:
            if idx == len(nums):
                if m_or == curr_or:
                    nonlocal result
                    result += 1
                return
            dfs(idx+1, curr_or | nums[idx])
            dfs(idx+1, curr_or)

        result = 0
        dfs()
        return result


def main():
    nums = [3, 1]
    assert Solution().countMaxOrSubsets(nums) == 2

    nums = [2, 2, 2]
    assert Solution().countMaxOrSubsets(nums) == 7


if __name__ == '__main__':
    main()
