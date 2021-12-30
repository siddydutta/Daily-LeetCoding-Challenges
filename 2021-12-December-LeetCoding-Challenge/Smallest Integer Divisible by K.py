# -*- coding: utf-8 -*-
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        ''' Straightforward brute force solution. '''
        if k % 2 == 0 or k % 5 == 0:
            return -1  # 111...111 can't be even or divisible by 5
        mod = 0
        # Increase number of digits until remainder is 0
        for n in range(1, k+1):
            mod = (mod*10 + 1) % k
            if mod == 0:
                return n
        return -1


def main():
    k = 1
    assert Solution().smallestRepunitDivByK(k) == 1

    k = 2
    assert Solution().smallestRepunitDivByK(k) == -1

    k = 3
    assert Solution().smallestRepunitDivByK(k) == 3

    k = 10**5-1
    assert Solution().smallestRepunitDivByK(k) == 45


if __name__ == '__main__':
    main()
