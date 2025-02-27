class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        nums = set(arr)
        max_len = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                n1, n2 = arr[i], arr[j]
                length = 0
                while n1 + n2 in nums:
                    n1, n2 = n2, n1 + n2
                    length += 1
                max_len = max(max_len, length)
        return max_len + 2 if max_len > 0 else max_len


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert Solution().lenLongestFibSubseq(arr) == 5

    arr = [1, 3, 7, 11, 12, 14, 18]
    assert Solution().lenLongestFibSubseq(arr) == 3


if __name__ == '__main__':
    main()
