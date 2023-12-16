class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


def main():
    s, t = 'anagram', 'nagaram'
    assert Solution().isAnagram(s, t)

    s, t = 'rat', 'car'
    assert not Solution().isAnagram(s, t)


if __name__ == '__main__':
    main()
