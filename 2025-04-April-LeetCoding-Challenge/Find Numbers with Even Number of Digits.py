class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum([len(str(num)) % 2 == 0 for num in nums])


def main():
    nums = [12, 345, 2, 6, 7896]
    assert Solution().findNumbers(nums) == 2

    nums = [555, 901, 482, 1771]
    assert Solution().findNumbers(nums) == 1


if __name__ == '__main__':
    main()
