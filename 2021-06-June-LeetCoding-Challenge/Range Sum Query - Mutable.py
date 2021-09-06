from typing import List, Tuple


class NumArray1:
    '''
    Naive solution, leads to TLE.
    Update: O(1)
    Query: O(n)
    '''
    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


class NumArray2:
    '''
    Another naive solution, to store sum from start to index i, leads to TLE.
    Update: O(n)
    Query: O(1)
    '''
    def __init__(self, nums: List[int]):
        self.sums = list()
        sum_so_far = 0
        for num in nums:
            sum_so_far += num
            self.sums.append(sum_so_far)

    def update(self, index: int, val: int) -> None:
        prev_sum = 0 if index == 0 else self.sums[index-1]
        curr_sum = self.sums[index]
        current_number = curr_sum - prev_sum
        difference = current_number - val
        for i in range(index, len(self.sums)):
            self.sums[i] -= difference

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]


class NumArray3:
    '''
    Simple Pythonic solution. Accepted answer.
    '''
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.total = sum(nums)

    def update(self, index: int, val: int) -> None:
        if not self.nums[index] == val:  # If new value is not the same as old
            # Update total
            self.total -= self.nums[index]
            self.total += val
            # Update nums
            self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        # Sum of range is total - {numbers before left} - {numbers after right}
        return self.total - sum(self.nums[:left]) - sum(self.nums[right+1:])


class NumArray:
    '''
    Using (binary) segment trees, appropriate for mutable range queries.
    In segment trees - leaf nodes represent the elements of the array, while
    each internal node represents some merging of the leaf nodes. In this case,
    an internal node's merge property is the sum of its child nodes.
    Update: O(log n)
    Query: O(log n)
    '''
    class Node:
        def __init__(self, lx, rx):
            '''
            lx, rx denotes the range of the interval of the node.
            left and right denote the children nodes.
            sum denotes the merge value.
            '''
            self.lx = lx
            self.rx = rx
            self.left = None
            self.right = None
            self.sum = 0

    def __buildTree(self, arr: List[int], i: int, j: int) -> Node:
        if i == j:  # Leaf node condition
            root = self.Node(i, j)
            root.sum = arr[i]
        else:  # Interval nodes
            root = self.Node(i, j)
            mid = i + (j - i) // 2
            root.left = self.__buildTree(arr, i, mid)
            root.right = self.__buildTree(arr, mid+1, j)
            root.sum = root.left.sum + root.right.sum
        return root

    def __updateTree(self, root: Node, index: int, value: int) -> Node:
        if root.lx == index and root.rx == index:
            root.sum = value
        else:
            mid = root.lx + (root.rx - root.lx) // 2
            if index <= mid:
                root.left = self.__updateTree(root.left, index, value)
            else:
                root.right = self.__updateTree(root.right, index, value)
            root.sum = root.left.sum + root.right.sum
        return root

    def __checkOverlap(self, nodeInterval: Tuple[int],
                       queryInterval: Tuple[int]) -> int:
        ix, iy = nodeInterval
        jx, jy = queryInterval

        if ix >= jx and iy <= jy:  # Complete overlap
            return 0
        elif iy < jx or ix > jy:  # No overlap
            return 1
        else:  # Partial overlap
            return 2

    def __sumRange(self, root: Node, i: int, j: int) -> int:
        k = self.__checkOverlap((root.lx, root.rx), (i, j))
        if k == 0:
            return root.sum
        elif k == 1:
            return 0
        else:
            return self.__sumRange(root.left, i, j) + \
                self.__sumRange(root.right, i, j)

    def __init__(self, nums):
        self.root = self.__buildTree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        self.root = self.__updateTree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.__sumRange(self.root, left, right)


if __name__ == '__main__':
    obj = NumArray([1, 3, 5])
    assert obj.sumRange(0, 2) == 9
    obj.update(1, 2)
    assert obj.sumRange(0, 2) == 8
    assert obj.sumRange(1, 2) == 7

    obj = NumArray([2, 4, 6, 8, 10])
    assert obj.sumRange(0, 0) == 2
    assert obj.sumRange(4, 4) == 10
    assert obj.sumRange(0, 1) == 6
    assert obj.sumRange(1, 1) == 4
    assert obj.sumRange(1, 4) == 28

    obj = NumArray([9, -8])
    assert isinstance(obj, NumArray)
    assert obj.root.sum == 1
    assert obj.root.left.sum == 9
    assert obj.root.right.sum == -8
    assert not obj.root.left.left and not obj.root.left.right
    assert not obj.root.right.left and not obj.root.right.right
