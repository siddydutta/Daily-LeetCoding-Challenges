class Solution:
    def compressedString(self, word: str) -> str:
        curr_count = 0
        curr_char = None
        comp = ''
        for ch in word:
            if ch != curr_char:
                if curr_char is not None and curr_count > 0:
                    comp += f'{curr_count}{curr_char}'
                curr_char = ch
                curr_count = 1
            else:
                curr_count += 1
                if curr_count == 9:
                    comp += f'{curr_count}{curr_char}'
                    curr_count = 0
        comp += (f'{curr_count}{curr_char}' if curr_count > 0 else '')
        return comp


def main():
    word = 'abcde'
    assert Solution().compressedString(word) == '1a1b1c1d1e'

    word = 'aaaaaaaaaaaaaabb'
    assert Solution().compressedString(word) == '9a5a2b'


if __name__ == '__main__':
    main()
