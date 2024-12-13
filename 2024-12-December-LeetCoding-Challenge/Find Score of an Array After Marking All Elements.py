from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums_idx = [(num, idx) for idx, num in enumerate(nums)]
        nums_idx.sort(reverse=True)
        score = 0
        marked = set()
        while nums_idx:
            num, idx = nums_idx.pop()
            if idx in marked:
                continue
            score += num
            marked.add(idx)
            if idx > 0:
                marked.add(idx-1)
            if idx < len(nums)-1:
                marked.add(idx+1)
        return score


def main():
    nums = [2, 1, 3, 4, 5, 2]
    assert Solution().findScore(nums) == 7

    nums = [2, 3, 5, 1, 3, 2]
    assert Solution().findScore(nums) == 5


if __name__ == '__main__':
    main()
