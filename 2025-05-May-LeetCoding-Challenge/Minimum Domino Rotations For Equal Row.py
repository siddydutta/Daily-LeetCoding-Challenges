class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        for n in (tops[0], bottoms[0]):
            if all(n in pairs for pairs in zip(tops, bottoms)):
                return len(tops) - max(tops.count(n), bottoms.count(n))
        return -1


def main():
    tops = [2, 1, 2, 4, 2, 2]
    bottoms = [5, 2, 6, 2, 3, 2]
    assert Solution().minDominoRotations(tops, bottoms) == 2

    tops = [3, 5, 1, 2, 3]
    bottoms = [3, 6, 3, 3, 4]
    assert Solution().minDominoRotations(tops, bottoms) == -1


if __name__ == '__main__':
    main()
