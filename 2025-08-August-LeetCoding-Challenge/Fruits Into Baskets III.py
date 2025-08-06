class SegmentTree:
    def __init__(self, baskets: list[int]):
        self.baskets = baskets
        self.m = len(baskets)
        self.tree = [0] * (4 * self.m)
        self.build(0, 0, self.m - 1)

    def build(self, curr: int, left: int, right: int) -> None:
        if left == right:
            self.tree[curr] = self.baskets[left]
            return
        mid = (left + right) // 2
        self.build(curr * 2 + 1, left, mid)
        self.build(curr * 2 + 2, mid + 1, right)
        self.tree[curr] = max(self.tree[curr * 2 + 1], self.tree[curr * 2 + 2])

    def update(self, curr: int, left: int, right: int, idx: int) -> None:
        if left == right:
            self.tree[curr] = 0
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(curr * 2 + 1, left, mid, idx)
        else:
            self.update(curr * 2 + 2, mid + 1, right, idx)
        self.tree[curr] = max(self.tree[curr * 2 + 1], self.tree[curr * 2 + 2])

    def query(self, curr: int, left: int, right: int, x: int) -> int:
        if self.tree[curr] < x:
            return -1
        if left == right:
            return left
        mid = (left + right) // 2
        if self.tree[curr * 2 + 1] >= x:
            return self.query(curr * 2 + 1, left, mid, x)
        return self.query(curr * 2 + 2, mid + 1, right, x)


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        segment_tree = SegmentTree(baskets)
        unplaced = 0
        for fruit in fruits:
            idx = segment_tree.query(0, 0, segment_tree.m - 1, fruit)
            if idx == -1:
                unplaced += 1
            else:
                segment_tree.update(0, 0, segment_tree.m - 1, idx)
        return unplaced


def main():
    fruits = [4, 2, 5]
    baskets = [3, 5, 4]
    assert Solution().numOfUnplacedFruits(fruits, baskets) == 1

    fruits = [3, 6, 1]
    baskets = [6, 4, 7]
    assert Solution().numOfUnplacedFruits(fruits, baskets) == 0


if __name__ == '__main__':
    main()
