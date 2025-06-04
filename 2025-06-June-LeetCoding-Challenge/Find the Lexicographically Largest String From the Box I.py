class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            # no split possible
            return word
        n = len(word)
        # brute force
        return max([word[i: i + n - (numFriends - 1)] for i in range(n)])


def main():
    word = 'dbca'
    numFriends = 2
    assert Solution().answerString(word, numFriends) == 'dbc'

    word = 'gggg'
    numFriends = 4
    assert Solution().answerString(word, numFriends) == 'g'


if __name__ == '__main__':
    main()
