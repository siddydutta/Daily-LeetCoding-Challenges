from typing import Tuple


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            return self.maximumGain(s[::-1], y, x)

        def count_substring(
                s: str, c1: str, c2: str, points: int
        ) -> Tuple[int, list]:
            stack, score = list(), 0
            for ch in s:
                if not stack or ch != c2:
                    stack.append(ch)
                elif stack[-1] == c1:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)
            return score, stack

        ab_points, stack = count_substring(s, 'a', 'b', x)
        ba_points, _ = count_substring(''.join(stack), 'b', 'a', y)
        return ab_points + ba_points


def main():
    s = 'cdbcbbaaabab'
    x = 4
    y = 5
    assert Solution().maximumGain(s, x, y) == 19

    s = 'aabbaaxybbaabb'
    x = 5
    y = 4
    assert Solution().maximumGain(s, x, y) == 20
