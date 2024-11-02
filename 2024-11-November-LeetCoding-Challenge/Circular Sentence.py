from itertools import pairwise


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        words.append(words[0])
        for w1, w2 in pairwise(words):
            if w1[-1] != w2[0]:
                return False
        return True


def main():
    sentence = 'leetcode exercises sound delightful'
    assert Solution().isCircularSentence(sentence) is True

    sentence = 'eetcode'
    assert Solution().isCircularSentence(sentence) is True

    sentence = 'Leetcode is cool'
    assert Solution().isCircularSentence(sentence) is False


if __name__ == '__main__':
    main()
