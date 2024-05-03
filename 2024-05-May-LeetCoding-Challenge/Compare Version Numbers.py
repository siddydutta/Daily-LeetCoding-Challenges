from itertools import zip_longest


class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1, v2 = list(map(int, v1.split('.'))), list(map(int, v2.split('.')))
        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 != rev2:
                return -1 if rev1 < rev2 else 1
        return 0


def main():
    version1 = '1.01'
    version2 = '1.001'
    assert Solution().compareVersion(version1, version2) == 0

    version1 = '1.0'
    version2 = '1.0.0'
    assert Solution().compareVersion(version1, version2) == 0

    version1 = '0.1'
    version2 = '1.1'
    assert Solution().compareVersion(version1, version2) == -1


if __name__ == '__main__':
    main()
