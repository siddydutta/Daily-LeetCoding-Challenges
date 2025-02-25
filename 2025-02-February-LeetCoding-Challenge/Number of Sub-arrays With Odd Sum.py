class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        num_odd, num_even = 0, 1
        curr = 0
        for num in arr:
            curr += num
            if curr & 1 == 0:
                num_even += 1
            else:
                num_odd += 1
        return (num_odd * num_even) % (10**9 + 7)


def main():
    arr = [1, 3, 5]
    assert Solution().numOfSubarrays(arr) == 4

    arr = [2, 4, 6]
    assert Solution().numOfSubarrays(arr) == 0

    arr = [1, 2, 3, 4, 5, 6, 7]
    assert Solution().numOfSubarrays(arr) == 16


if __name__ == '__main__':
    main()
