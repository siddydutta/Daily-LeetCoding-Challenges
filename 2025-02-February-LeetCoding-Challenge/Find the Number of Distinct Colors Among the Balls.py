class Solution:
    def queryResults(self, _: int, queries: list[list[int]]) -> list[int]:
        ball_color = dict()
        color_count = dict()
        result = []
        for ball, color in queries:
            if ball in ball_color:
                color_count[ball_color[ball]] -= 1
                if color_count[ball_color[ball]] == 0:
                    del color_count[ball_color[ball]]
            ball_color[ball] = color
            color_count[color] = color_count.get(color, 0) + 1
            result.append(len(color_count))
        return result


def main():
    limit = 4
    queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
    assert Solution().queryResults(limit, queries) == [1, 2, 2, 3]

    limit = 4
    queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
    assert Solution().queryResults(limit, queries) == [1, 2, 2, 3, 4]


if __name__ == '__main__':
    main()
