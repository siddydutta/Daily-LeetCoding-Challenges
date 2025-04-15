class BIT:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)

    def update(self, i: int, delta: int) -> None:
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i: int) -> int:
        res = 0
        i += 1
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res


class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        pos2 = {num: idx for idx, num in enumerate(nums2)}
        left, right = [0] * n, [0] * n

        bit = BIT(n)
        for y in nums1:
            j = pos2[y]
            left[y] = bit.query(j - 1)
            bit.update(j, 1)

        bit = BIT(n)
        for y in reversed(nums1):
            j = pos2[y]
            right[y] = bit.query(n - 1) - bit.query(j)
            bit.update(j, 1)

        return sum(l * r for l, r in zip(left, right))


def main():
    nums1 = [2, 0, 1, 3]
    nums2 = [0, 1, 2, 3]
    assert Solution().goodTriplets(nums1, nums2) == 1

    nums1 = [4, 0, 1, 3, 2]
    nums2 = [4, 1, 0, 2, 3]
    assert Solution().goodTriplets(nums1, nums2) == 4


if __name__ == '__main__':
    main()
