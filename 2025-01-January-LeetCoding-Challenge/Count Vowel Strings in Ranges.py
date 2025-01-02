from typing import List


class Solution:
    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        p_sums = [0]
        curr = 0
        for word in words:
            if word[0] in self.VOWELS and word[-1] in self.VOWELS:
                curr += 1
            p_sums.append(curr)
        return [p_sums[r + 1] - p_sums[l] for l, r in queries]


def main():
    words = ['aba', 'bcb', 'ece', 'aa', 'e']
    queries = [[0, 2], [1, 4], [1, 1]]
    assert Solution().vowelStrings(words, queries) == [2, 3, 0]

    words = ['a', 'e', 'i']
    queries = [[0, 2], [0, 1], [2, 2]]
    assert Solution().vowelStrings(words, queries) == [3, 2, 1]


if __name__ == '__main__':
    main()
