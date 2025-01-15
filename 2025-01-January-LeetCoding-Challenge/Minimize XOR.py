class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1, n2 = num1.bit_count(), num2.bit_count()
        res = num1
        for i in range(32):
            if n1 > n2 and (1 << i) & num1 > 0:
                res ^= 1 << i
                n1 -= 1
            if n1 < n2 and (1 << i) & num1 == 0:
                res ^= 1 << i
                n1 += 1
        return res


def main():
    num1 = 3
    num2 = 5
    assert Solution().minimizeXor(num1, num2) == 3

    num1 = 1
    num2 = 12
    assert Solution().minimizeXor(num1, num2) == 3


if __name__ == '__main__':
    main()
