class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        _min, _max = 0, 0
        curr = 0
        for diff in differences:
            curr += diff
            _min = min(_min, curr)
            _max = max(_max, curr)
        return max((upper - lower) - (_max - _min) + 1, 0)


def main():
    differences = [1, -3, 4]
    lower = 1
    upper = 6
    assert Solution().numberOfArrays(differences, lower, upper) == 2

    differences = [3, -4, 5, 1, -2]
    lower = -4
    upper = 5
    assert Solution().numberOfArrays(differences, lower, upper) == 4

    differences = [4, -7, 2]
    lower = 3
    upper = 6
    assert Solution().numberOfArrays(differences, lower, upper) == 0


if __name__ == '__main__':
    main()
