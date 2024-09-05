from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rem_sum = mean * (n + len(rolls)) - sum(rolls)
        if rem_sum < n or rem_sum > n*6:
            return []

        base, rem = divmod(rem_sum, n)
        return [base+1 if i < rem else base for i in range(n)]


def main():
    rolls = [3, 2, 4, 3]
    mean = 4
    n = 2
    assert Solution().missingRolls(rolls, mean, n) == [6, 6]

    rolls = [1, 5, 6]
    mean = 3
    n = 4
    assert Solution().missingRolls(rolls, mean, n) == [3, 2, 2, 2]

    rolls = [1, 2, 3, 4]
    mean = 6
    n = 4
    assert Solution().missingRolls(rolls, mean, n) == []


if __name__ == '__main__':
    main()
