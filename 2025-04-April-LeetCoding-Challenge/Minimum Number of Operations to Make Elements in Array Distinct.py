class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        frequencies, non_unique = dict(), set()
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
                non_unique.add(num)
            else:
                frequencies[num] = 1

        operations = 0
        while nums and non_unique:
            operations += 1
            for num in nums[:3]:
                frequency = frequencies[num] - 1
                if frequency == 1:
                    non_unique.remove(num)
                frequencies[num] = frequency
            nums = nums[3:]
        return operations


def main():
    nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
    assert Solution().minimumOperations(nums) == 2

    nums = [4, 5, 6, 4, 4]
    assert Solution().minimumOperations(nums) == 2

    nums = [6, 7, 8, 9]
    assert Solution().minimumOperations(nums) == 0


if __name__ == '__main__':
    main()
