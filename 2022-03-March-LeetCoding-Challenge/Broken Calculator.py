# -*- coding: utf-8 -*-
class Solution:
    def brokenCalc(self, start_value: int, target: int) -> int:
        ''' Greedy solution. '''
        if start_value >= target:
            # Decrement op until target
            return start_value - target

        ops = int()
        while start_value < target:
            ops += 1
            # Try division op
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
        # Ops so far + remaining decrement ops
        return start_value - target + ops


def main():
    start_value, target = 2, 3
    assert Solution().brokenCalc(start_value, target) == 2

    start_value, target = 5, 8
    assert Solution().brokenCalc(start_value, target) == 2

    start_value, target = 3, 10
    assert Solution().brokenCalc(start_value, target) == 3

    start_value, target = 1234, 1
    assert Solution().brokenCalc(start_value, target) == 1233


if __name__ == '__main__':
    main()
