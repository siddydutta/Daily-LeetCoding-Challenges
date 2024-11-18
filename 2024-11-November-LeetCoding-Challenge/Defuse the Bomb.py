from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if k == 0:
            return result

        for i in range(n):
            if k > 0:
                result[i] = sum(code[(i+j) % n] for j in range(1, k+1))
            elif k < 0:
                result[i] = sum(code[(i+j) % n] for j in range(-1, k-1, -1))
        return result


def main():
    code = [5, 7, 1, 4]
    k = 3
    assert Solution().decrypt(code, k) == [12, 10, 16, 13]

    code = [1, 2, 3, 4]
    k = 0
    assert Solution().decrypt(code, k) == [0, 0, 0, 0]

    code = [2, 4, 9, 3]
    k = -2
    assert Solution().decrypt(code, k) == [12, 5, 6, 13]


if __name__ == '__main__':
    main()
