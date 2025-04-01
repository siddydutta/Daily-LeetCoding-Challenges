from functools import lru_cache


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:

        @lru_cache(None)
        def dfs(idx: int = 0) -> int:
            if idx >= len(questions):
                return 0
            points, brainpower = questions[idx]
            return max(dfs(idx + 1), points + dfs(idx + brainpower + 1))
        return dfs()


def main():
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    assert Solution().mostPoints(questions) == 5

    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    assert Solution().mostPoints(questions) == 7


if __name__ == '__main__':
    main()
