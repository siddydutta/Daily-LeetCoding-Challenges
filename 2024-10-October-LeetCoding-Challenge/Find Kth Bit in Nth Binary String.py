class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        length = 2**(n-1) - 1
        if k == length+1:
            return '1'
        elif k <= length:
            return self.findKthBit(n-1, k)
        else:
            bit = self.findKthBit(n-1, 2*length+2-k)
            return '1' if bit == '0' else '0'


def main():
    n = 3
    k = 1
    assert Solution().findKthBit(n, k) == '0'

    n = 4
    k = 11
    assert Solution().findKthBit(n, k) == '1'


if __name__ == '__main__':
    main()
