from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = list()
        target_set = set(target)
        for i in range(1, target[-1]+1):
            ops.append("Push")
            if i not in target_set:
                ops.append("Pop")
        return ops


def main():
    target = [1, 3]
    n = 3
    assert Solution().buildArray(target, n) == ["Push", "Push", "Pop", "Push"]

    target = [1, 2, 3]
    n = 3
    assert Solution().buildArray(target, n) == ["Push", "Push", "Push"]

    target = [1, 2]
    n = 4
    assert Solution().buildArray(target, n) == ["Push", "Push"]


if __name__ == '__main__':
    main()
