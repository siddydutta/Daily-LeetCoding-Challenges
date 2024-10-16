class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        string = ''
        n_a, n_b, n_c = 0, 0, 0
        for _ in range(a + b + c):
            if (a >= b and a >= c and n_a < 2) or \
               (n_b == 2 and a > 0 and n_a < 2) or \
               (n_c == 2 and a > 0 and n_a < 2):
                string += 'a'
                a -= 1
                n_a += 1
                n_b, n_c = 0, 0
            elif (b >= a and b >= c and n_b < 2) or \
                 (n_a == 2 and b > 0 and n_b < 2) or \
                 (n_c == 2 and b > 0 and n_b < 2):
                string += 'b'
                b -= 1
                n_b += 1
                n_a, n_c = 0, 0
            elif (c >= a and c >= b and n_c < 2) or \
                 (n_a == 2 and c > 0 and n_c < 2) or \
                 (n_b == 2 and c > 0 and n_c < 2):
                string += 'c'
                c -= 1
                n_c += 1
                n_a, n_b = 0, 0
        return string


def main():
    a = 1
    b = 1
    c = 7
    assert Solution().longestDiverseString(a, b, c) == 'ccaccbcc'

    a = 7
    b = 1
    c = 0
    assert Solution().longestDiverseString(a, b, c) == 'aabaa'


if __name__ == '__main__':
    main()
