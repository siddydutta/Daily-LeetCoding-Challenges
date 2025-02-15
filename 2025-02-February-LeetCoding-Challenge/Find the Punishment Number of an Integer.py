class Solution:
    def punishmentNumber(self, n: int) -> int:

        def can_partition(s: str, target: int) -> bool:
            if not s and target == 0:
                return True
            if target < 0:
                return False
            for i in range(len(s)):
                left = int(s[:i+1])
                right = s[i+1:]
                if can_partition(right, target - left):
                    return True
            return False

        sum_ = 0
        for num in range(1, n+1):
            sqr = num * num
            if can_partition(str(sqr), num):
                sum_ += sqr
        return sum_


def main():
    n = 10
    assert Solution().punishmentNumber(n) == 182

    n = 37
    assert Solution().punishmentNumber(n) == 1478


if __name__ == '__main__':
    main()
