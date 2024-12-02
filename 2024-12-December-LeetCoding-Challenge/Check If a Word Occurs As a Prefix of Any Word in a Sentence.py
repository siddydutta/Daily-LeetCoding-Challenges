class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(sentence.split(), start=1):
            if word.startswith(searchWord):
                return idx
        return -1


def main():
    sentence = 'i love eating burger'
    searchWord = 'burg'
    assert Solution().isPrefixOfWord(sentence, searchWord) == 4

    sentence = 'this problem is an easy problem'
    searchWord = 'pro'
    assert Solution().isPrefixOfWord(sentence, searchWord) == 2

    sentence = 'i am tired'
    searchWord = 'you'
    assert Solution().isPrefixOfWord(sentence, searchWord) == -1


if __name__ == '__main__':
    main()
