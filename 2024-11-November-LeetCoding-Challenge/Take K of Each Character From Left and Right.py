class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = [0, 0, 0]
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        if min(counts) < k:
            return -1

        res = float('inf')
        left = 0
        for right in range(len(s)):
            counts[ord(s[right]) - ord('a')] -= 1
            while min(counts) < k:
                counts[ord(s[left]) - ord('a')] += 1
                left += 1
            res = min(res, len(s)-(right-left+1))
        return res


def main():
    s = 'aabaaaacaabc'
    k = 2
    assert Solution().takeCharacters(s, k) == 8

    s = 'a'
    k = 1
    assert Solution().takeCharacters(s, k) == -1


if __name__ == '__main__':
    main()
