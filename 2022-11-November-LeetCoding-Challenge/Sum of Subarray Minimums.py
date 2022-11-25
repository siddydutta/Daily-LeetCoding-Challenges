# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, result = list(), [0]*len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1] if stack else -1
            result[i] = result[j] + (i-j)*arr[i]
            stack.append(i)
        return sum(result) % (10**9+7)


def main():
    arr = [3, 1, 2, 4]
    assert Solution().sumSubarrayMins(arr) == 17

    arr = [11, 81, 94, 43, 3]
    assert Solution().sumSubarrayMins(arr) == 444


if __name__ == '__main__':
    main()
