# -*- coding: utf-8 -*-
class Solution:
    ''' Straightforward Pythonic solution. '''
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


def main():
    s = "the sky is blue"
    assert Solution().reverseWords(s) == "blue is sky the"

    s = "  hello world  "
    assert Solution().reverseWords(s) == "world hello"

    s = "a good   example"
    assert Solution().reverseWords(s) == "example good a"

    s = "  Bob    Loves  Alice   "
    assert Solution().reverseWords(s) == "Alice Loves Bob"

    s = "Alice does not even like bob"
    assert Solution().reverseWords(s) == "bob like even not does Alice"


if __name__ == '__main__':
    main()
