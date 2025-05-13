class Solution:
    MOD = 10**9 + 7

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counts = [0] * 27
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        for _ in range(t):
            for i in range(25, -1, -1):
                counts[i + 1] = counts[i]
            counts[0] = 0  # reset a
            if counts[26]:
                # split z into a and b
                counts[0] += counts[26] % self.MOD
                counts[1] += counts[26] % self.MOD
                counts[26] = 0
        return sum(counts) % self.MOD


def main():
    s = 'abcyy'
    t = 2
    assert Solution().lengthAfterTransformations(s, t) == 7

    s = 'azbk'
    t = 1
    assert Solution().lengthAfterTransformations(s, t) == 5


if __name__ == '__main__':
    main()
