class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            idx = word.index(ch)
        except ValueError:
            return word
        return word[:idx+1][::-1] + word[idx+1:]


def main():
    word = "abcdefd"
    ch = "d"
    assert Solution().reversePrefix(word, ch) == "dcbaefd"

    word = "xyxzxe"
    ch = "z"
    assert Solution().reversePrefix(word, ch) == "zxyxxe"

    word = "abcd"
    ch = "z"
    assert Solution().reversePrefix(word, ch) == "abcd"


if __name__ == '__main__':
    main()
