from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequency = [0] * k
        for num in arr:
            num %= k
            if num < 0:
                num += k
            frequency[num] += 1

        if frequency[0] % 2 != 0:
            return False
        for i in range(1, (k//2)+1):
            if frequency[i] != frequency[k-i]:
                return False
        return True


def main():
    arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    k = 5
    assert Solution().canArrange(arr, k) is True

    arr = [1, 2, 3, 4, 5, 6]
    k = 7
    assert Solution().canArrange(arr, k) is True

    arr = [1, 2, 3, 4, 5, 6]
    k = 10
    assert Solution().canArrange(arr, k) is False


if __name__ == '__main__':
    main()
