class Solution:
    def point_to_vowel(self, string: str, start: int, reverse: bool) -> int:
        loop = range(start, -1, -1) if reverse else range(start, len(string))
        for idx in loop:
            if string[idx].lower() in {'a', 'e', 'i', 'o', 'u'}:
                return idx
        return None

    def reverseVowels(self, s: str) -> str:
        ptr1 = self.point_to_vowel(s, 0, False)
        ptr2 = self.point_to_vowel(s, len(s)-1, True)
        string = list(s)
        while ptr1 is not None and ptr2 is not None and ptr1 < ptr2:
            string[ptr1], string[ptr2] = string[ptr2], string[ptr1]
            ptr1 = self.point_to_vowel(s, ptr1+1, False)
            ptr2 = self.point_to_vowel(s, ptr2-1, True)
        return "".join(string)


def main():
    s = "hello"
    assert Solution().reverseVowels(s) == "holle"

    s = "leetcode"
    assert Solution().reverseVowels(s) == "leotcede"

    s = "ai"
    assert Solution().reverseVowels(s) == "ia"


if __name__ == '__main__':
    main()
