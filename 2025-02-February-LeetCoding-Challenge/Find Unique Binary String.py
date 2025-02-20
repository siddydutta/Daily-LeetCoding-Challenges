class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        for i in range(2**n):
            bin_str = (bin(i)[2:]).zfill(n)
            if bin_str not in nums:
                return bin_str


def main():
    nums = ['01', '10']
    assert Solution().findDifferentBinaryString(nums) == '00'

    nums = ['00', '01']
    assert Solution().findDifferentBinaryString(nums) == '10'

    nums = ['111', '011', '001']
    assert Solution().findDifferentBinaryString(nums) == '000'


if __name__ == '__main__':
    main()
