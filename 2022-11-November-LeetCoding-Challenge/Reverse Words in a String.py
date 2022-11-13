from typing import List


class Solution:
    def __reverse(self, char: List[str], ptr1: int, ptr2: int) -> None:
        ''' Reverses characters between two indices of a character array. '''
        while ptr1 < ptr2:
            char[ptr1], char[ptr2] = char[ptr2], char[ptr1]
            ptr1 += 1
            ptr2 -= 1

    def reverseWords(self, s: str) -> str:
        chars, n = list(s), len(s)
        # reverse entire string
        self.__reverse(chars, 0, n - 1)
        ptr1, ptr2 = 0, 0
        while ptr1 < n:
            # find ending of current word
            while ptr2 < n and not chars[ptr2].isspace():
                ptr2 += 1
            # reverse current word
            self.__reverse(chars, ptr1, ptr2 - 1)
            ptr1 = ptr2
            # find beginnning of next word
            while ptr1 < n and chars[ptr1].isspace():
                ptr1 += 1
            ptr2 = ptr1 + 1

        # remove leading spaces
        ptr = 0
        while ptr < len(chars) and chars[ptr].isspace():
            chars.pop(ptr)
        # remove extra spaces
        ptr = 1
        while ptr < len(chars):
            if chars[ptr - 1].isspace() and chars[ptr].isspace():
                chars.pop(ptr)
            else:
                ptr += 1
        # remove trailing spaces
        ptr = len(chars) - 1
        while ptr >= 0 and chars[ptr].isspace():
            chars.pop(ptr)
            ptr -= 1
        return "".join(chars)
        # return " ".join(reversed(s.split()))  # trivial solution


def main():
    s = "the sky is blue"
    assert Solution().reverseWords(s) == "blue is sky the"

    s = "  hello world  "
    assert Solution().reverseWords(s) == "world hello"

    s = "a good   example"
    assert Solution().reverseWords(s) == "example good a"


if __name__ == '__main__':
    main()
