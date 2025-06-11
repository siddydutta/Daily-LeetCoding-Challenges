from itertools import permutations


class Solution:
    def __get_status(self, n1: int, n2: int) -> int:
        return ((n1 & 1) << 1) | (n2 & 1)

    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = float('-inf')
        for a, b in permutations('01234', 2):
            best = [float('inf')] * 4
            cnt_a, cnt_b = 0, 0
            prev_a, prev_b = 0, 0
            ptr1 = -1
            for ptr2 in range(n):
                cnt_a += s[ptr2] == a
                cnt_b += s[ptr2] == b
                while ptr2 - ptr1 >= k and cnt_b - prev_b >= 2:
                    left_status = self.__get_status(prev_a, prev_b)
                    best[left_status] = min(best[left_status], prev_a - prev_b)
                    ptr1 += 1
                    prev_a += s[ptr1] == a
                    prev_b += s[ptr1] == b
                right_status = self.__get_status(cnt_a, cnt_b)
                if best[right_status ^ 0b10] != float('inf'):
                    ans = max(ans, cnt_a - cnt_b - best[right_status ^ 0b10])
        return ans


def main():
    s = '12233'
    k = 4
    assert Solution().maxDifference(s, k) == -1

    s = '1122211'
    k = 3
    assert Solution().maxDifference(s, k) == 1

    s = '110'
    k = 3
    assert Solution().maxDifference(s, k) == -1


if __name__ == '__main__':
    main()
