class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        idx = 1
        while time != 0:
            time -= 1
            idx += direction
            if idx == 1 or idx == n:
                direction *= -1
        return idx


def main():
    n = 4
    time = 5
    assert Solution().passThePillow(n, time) == 2

    n = 3
    time = 2
    assert Solution().passThePillow(n, time) == 3


if __name__ == '__main__':
    main()
