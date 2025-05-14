from itertools import product


class Solution:
    MOD = 10**9 + 7

    def __multiply_matrices(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        p, q, r = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * r for _ in range(p)]
        for i, j in product(range(p), range(r)):
            temp = 0
            for k in range(q):
                temp += mat1[i][k] * mat2[k][j]
            result[i][j] = temp % self.MOD
        return result

    def __power_matrix(self, matrix: list[list[int]], exp: int) -> list[list[int]]:
        n = len(matrix)
        result = [[int(i == j) for j in range(n)] for i in range(n)]
        while exp > 0:
            if exp & 1:
                result = self.__multiply_matrices(result, matrix)
            matrix = self.__multiply_matrices(matrix, matrix)
            exp >>= 1
        return result

    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        transform = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for shift in range(nums[i]):
                transform[i][(i + 1 + shift) % 26] += 1
        transform = self.__power_matrix(transform, t)

        freqs = [[0] * 26]
        for ch in s:
            freqs[0][ord(ch) - ord('a')] += 1
        freqs = self.__multiply_matrices(freqs, transform)
        return sum(freqs[0]) % self.MOD


def main():
    s = 'abcyy'
    t = 2
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    assert Solution().lengthAfterTransformations(s, t, nums) == 7

    s = 'azbk'
    t = 1
    nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert Solution().lengthAfterTransformations(s, t, nums) == 8


if __name__ == '__main__':
    main()
