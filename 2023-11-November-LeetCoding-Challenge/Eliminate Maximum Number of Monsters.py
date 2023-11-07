from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_to_arrive = sorted([d / s for d, s in zip(dist, speed)])
        for i, time in enumerate(time_to_arrive):
            if time <= i:
                return i
        return len(time_to_arrive)


def main():
    dist = [1, 3, 4]
    speed = [1, 1, 1]
    assert Solution().eliminateMaximum(dist, speed) == 3

    dist = [1, 1, 2, 3]
    speed = [1, 1, 1, 1]
    assert Solution().eliminateMaximum(dist, speed) == 1

    dist = [3, 2, 4]
    speed = [5, 3, 2]
    assert Solution().eliminateMaximum(dist, speed) == 1


if __name__ == '__main__':
    main()
