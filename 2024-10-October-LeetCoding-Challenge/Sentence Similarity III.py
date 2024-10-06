from collections import deque


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        dq1, dq2 = map(deque, (map(str.split, (sentence1, sentence2))))
        # remove common prefix
        while dq1 and dq2 and dq1[0] == dq2[0]:
            dq1.popleft()
            dq2.popleft()
        # remove common suffix
        while dq1 and dq2 and dq1[-1] == dq2[-1]:
            dq1.pop()
            dq2.pop()
        return not dq1 or not dq2


def main():
    sentence1 = 'My name is Haley'
    sentence2 = 'My Haley'
    assert Solution().areSentencesSimilar(sentence1, sentence2) is True

    sentence1 = 'of'
    sentence2 = 'A lot of words'
    assert Solution().areSentencesSimilar(sentence1, sentence2) is False

    sentence1 = 'Eating right now'
    sentence2 = 'Eating'
    assert Solution().areSentencesSimilar(sentence1, sentence2) is True


if __name__ == '__main__':
    main()
