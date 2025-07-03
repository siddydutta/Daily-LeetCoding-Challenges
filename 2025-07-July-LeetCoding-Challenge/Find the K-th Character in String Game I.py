class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            size = len(word)
            for i in range(size):
                word += (chr(97 + ((ord(word[i]) - 97 + 1) % 26)))
        return word[k - 1]


def main():
    k = 5
    assert Solution().kthCharacter(k) == 'b'

    k = 10
    assert Solution().kthCharacter(k) == 'c'


if __name__ == '__main__':
    main()
