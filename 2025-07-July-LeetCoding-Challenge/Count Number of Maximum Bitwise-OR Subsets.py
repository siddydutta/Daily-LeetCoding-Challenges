class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        m_or = 0
        for num in nums:
            m_or |= num
        result = 0

        def dfs(idx: int, curr_or: int) -> None:
            if idx == len(nums):
                if m_or == curr_or:
                    nonlocal result
                    result += 1
                return
            dfs(idx + 1, curr_or | nums[idx])
            dfs(idx + 1, curr_or)

        dfs(0, 0)
        return result


def main():
    nums = [3, 1]
    assert Solution().countMaxOrSubsets(nums) == 2

    nums = [2, 2, 2]
    assert Solution().countMaxOrSubsets(nums) == 7

    nums = [3, 2, 1, 5]
    assert Solution().countMaxOrSubsets(nums) == 6


if __name__ == '__main__':
    main()
