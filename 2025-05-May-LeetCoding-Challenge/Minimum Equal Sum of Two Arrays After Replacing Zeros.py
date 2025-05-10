class Solution:
    def __sum_and_zeros(self, nums: list[int]) -> tuple[int, int]:
        sum_, count = 0, 0
        for num in nums:
            sum_ += num
            count += num == 0
        return sum_, count

    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        (s1, z1), (s2, z2) = map(self.__sum_and_zeros, (nums1, nums2))
        min_sum1, min_sum2 = s1 + z1, s2 + z2
        if z1 == 0 and s1 < min_sum2:
            return -1
        if z2 == 0 and s2 < min_sum1:
            return -1
        return max(min_sum1, min_sum2)


def main():
    nums1 = [3, 2, 0, 1, 0]
    nums2 = [6, 5, 0]
    assert Solution().minSum(nums1, nums2) == 12

    nums1 = [2, 0, 2, 0]
    nums2 = [1, 4]
    assert Solution().minSum(nums1, nums2) == -1


if __name__ == '__main__':
    main()
