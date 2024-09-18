from typing import List


class Num:
    def __init__(self, num: int):
        self.num = str(num)

    def __lt__(self, other: 'Num') -> bool:
        # when comparing 10 & 2 => 102 < 210
        return self.num + other.num < other.num + self.num

    def __str__(self) -> str:
        return self.num


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(list(map(Num, nums)), reverse=True)
        if str(nums[0]) == '0':
            return '0'
        return ''.join(map(str, nums))


def main():
    nums = [10, 2]
    assert Solution().largestNumber(nums) == '210'

    nums = [3, 30, 34, 5, 9]
    assert Solution().largestNumber(nums) == '9534330'


if __name__ == '__main__':
    main()
