class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return not seen


def main():
    nums = [3, 2, 3, 2, 2, 2]
    assert Solution().divideArray(nums) is True

    nums = [1, 2, 3, 4]
    assert Solution().divideArray(nums) is False


if __name__ == '__main__':
    main()
