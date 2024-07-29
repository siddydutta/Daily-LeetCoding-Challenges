from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        for i, val in enumerate(rating[1:-1], start=1):
            left_lt, left_gt = 0, 0
            for left in rating[:i]:
                if left < val:
                    left_lt += 1
                else:
                    left_gt += 1
            right_lt, right_gt = 0, 0
            for right in rating[i+1:]:
                if right < val:
                    right_lt += 1
                else:
                    right_gt += 1
            teams += (left_lt*right_gt) + (left_gt*right_lt)
        return teams


def main():
    rating = [2, 5, 3, 4, 1]
    assert Solution().numTeams(rating) == 3

    rating = [2, 1, 3]
    assert Solution().numTeams(rating) == 0

    rating = [1, 2, 3, 4]
    assert Solution().numTeams(rating) == 4


if __name__ == '__main__':
    main()
