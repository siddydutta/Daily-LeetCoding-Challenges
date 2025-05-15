class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        return [word for i, word in enumerate(words) if i == 0 or groups[i] != groups[i - 1]]


def main():
    words = ['e', 'a', 'b']
    groups = [0, 0, 1]
    assert Solution().getLongestSubsequence(words, groups) == ['e', 'b']

    words = ['a', 'b', 'c', 'd']
    groups = [1, 0, 1, 1]
    assert Solution().getLongestSubsequence(words, groups) == ['a', 'b', 'c']


if __name__ == '__main__':
    main()
