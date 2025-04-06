class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count, previous = [0] * n, [0] * n
        nums.sort()

        max_count, index = 0, -1
        for i in range(n):
            count[i], previous[i] = 1, -1
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and count[j] + 1 > count[i]:
                    count[i] = count[j] + 1
                    previous[i] = j
            if count[i] > max_count:
                max_count = count[i]
                index = i

        subset = []
        while index != -1:
            subset.append(nums[index])
            index = previous[index]
        return subset


def main():
    nums = [1, 2, 3]
    assert Solution().largestDivisibleSubset(nums) == [2, 1]

    nums = [1, 2, 4, 8]
    assert Solution().largestDivisibleSubset(nums) == [8, 4, 2, 1]


if __name__ == '__main__':
    main()
