from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = map(sorted, (g, s))
        count = 0
        while g and s:
            if s[-1] >= g[-1]:
                count += 1
                s.pop()
            g.pop()
        return count


def main():
    g = [1, 2, 3]
    s = [1, 1]
    assert Solution().findContentChildren(g, s) == 1

    g = [1, 2]
    s = [1, 2, 3]
    assert Solution().findContentChildren(g, s) == 2


if __name__ == '__main__':
    main()
