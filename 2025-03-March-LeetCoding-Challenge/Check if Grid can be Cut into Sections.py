class Solution:
    def __calculate_boundaries(self, rectangles: list[list[int]], dim: int) -> list[tuple[int, int]]:
        boundaries = [(rectangle[dim], rectangle[dim+2]) for rectangle in rectangles]
        boundaries.sort()
        return boundaries

    def __line_sweep(self, lines: list[tuple[int, int]]) -> bool:
        n_lines = 0
        last = lines[0][1]
        for start, end in lines:
            if start >= last:
                n_lines += 1
                if n_lines == 2:
                    return True
            last = max(last, end)
        return False

    def checkValidCuts(self, _: int, rectangles: list[list[int]]) -> bool:
        h_lines = self.__calculate_boundaries(rectangles, 1)
        v_lines = self.__calculate_boundaries(rectangles, 0)
        return self.__line_sweep(h_lines) or self.__line_sweep(v_lines)


def main():
    n = 5
    rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
    assert Solution().checkValidCuts(n, rectangles) is True

    n = 4
    rectangles = [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]
    assert Solution().checkValidCuts(n, rectangles) is True

    n = 4
    rectangles = [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]
    assert Solution().checkValidCuts(n, rectangles) is False


if __name__ == '__main__':
    main()
