class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        return t >= max(abs(fy-sy), abs(fx-sx))


def main():
    sx, sy, fx, fy, t = 2, 4, 7, 7, 6
    assert Solution().isReachableAtTime(sx, sy, fx, fy, t)

    sx, sy, fx, fy, t = 3, 1, 7, 3, 3
    assert not Solution().isReachableAtTime(sx, sy, fx, fy, t)


if __name__ == '__main__':
    main()
