class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total_area = (ax1 - ax2)*(ay1 - ay2) + (bx1 - bx2)*(by1 - by2)
        overlap = max(min(ax2, bx2)-max(ax1, bx1), 0) * max(min(ay2, by2)-max(ay1, by1), 0)
        return total_area - overlap


def main():
    ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = -3, 0, 3, 4, 0, -1, 9, 2
    assert Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == 45

    ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = -2, -2, 2, 2, -2, -2, 2, 2
    assert Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == 16


if __name__ == '__main__':
    main()
