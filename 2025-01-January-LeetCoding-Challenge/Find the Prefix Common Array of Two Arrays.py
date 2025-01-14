from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C, count, seen = [], 0, set()
        for a, b in zip(A, B):
            if a in seen:
                count += 1
            else:
                seen.add(a)
            if b in seen:
                count += 1
            else:
                seen.add(b)
            C.append(count)
        return C


def main():
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    assert Solution().findThePrefixCommonArray(A, B) == [0, 2, 3, 4]

    A = [2, 3, 1]
    B = [3, 1, 2]
    assert Solution().findThePrefixCommonArray(A, B) == [0, 1, 3]


if __name__ == '__main__':
    main()
