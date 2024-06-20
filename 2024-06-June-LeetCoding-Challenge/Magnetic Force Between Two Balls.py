from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def feasible(distance: int) -> bool:
            # check if it is possible to place m balls with distance
            count = 1
            last = position[0]
            for i in range(1, len(position)):
                if position[i]-last >= distance:
                    count += 1
                    last = position[i]
                    if count == m:
                        return True
            return False

        position.sort()
        left = 1  # min possible distance
        right = position[-1]-position[0]  # max possible distance
        while left <= right:
            mid = left + (right-left)//2
            if feasible(mid):
                # try for a larger distance
                left = mid+1
            else:
                # try for a smaller distance
                right = mid-1
        return right


def main():
    position = [1, 2, 3, 4, 7]
    m = 3
    assert Solution().maxDistance(position, m) == 3

    position = [5, 4, 3, 2, 1, 1000000000]
    m = 2
    assert Solution().maxDistance(position, m) == 999999999

    position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = 4
    assert Solution().maxDistance(position, m) == 3


if __name__ == '__main__':
    main()
