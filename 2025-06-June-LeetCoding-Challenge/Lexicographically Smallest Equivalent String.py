class UnionFind:
    def __init__(self):
        self.parent = dict()

    def find(self, x: str) -> str:
        if x not in self.parent:
            self.parent[x] = x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x < root_y:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union_find = UnionFind()
        for ch1, ch2 in zip(s1, s2):
            union_find.union(ch1, ch2)
        return ''.join([union_find.find(ch) for ch in baseStr])


def main():
    s1 = 'parker'
    s2 = 'morris'
    baseStr = 'parser'
    assert Solution().smallestEquivalentString(s1, s2, baseStr) == 'makkek'

    s1 = 'hello'
    s2 = 'world'
    baseStr = 'hold'
    assert Solution().smallestEquivalentString(s1, s2, baseStr) == 'hdld'

    s1 = 'leetcode'
    s2 = 'programs'
    baseStr = 'sourcecode'
    assert Solution().smallestEquivalentString(s1, s2, baseStr) == 'aauaaaaada'


if __name__ == '__main__':
    main()
