from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        subs = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    subs.append(words[i])
                    break
        return subs


def main():
    words = ['mass', 'as', 'hero', 'superhero']
    assert Solution().stringMatching(words) == ['as', 'hero']

    words = ['leetcode', 'et', 'code']
    assert Solution().stringMatching(words) == ['et', 'code']


if __name__ == '__main__':
    main()
