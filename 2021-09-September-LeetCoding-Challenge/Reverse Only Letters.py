# -*- coding: utf-8 -*-
class Solution:
    ''' Time Complexity: O(n) '''
    def reverseOnlyLetters(self, s: str) -> str:
        string = list(s)
        # Two-pointer approach
        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            # Find characters to swap
            while left_ptr < len(s) and not string[left_ptr].isalpha():
                left_ptr += 1
            while right_ptr >= 0 and not string[right_ptr].isalpha():
                right_ptr -= 1
            if left_ptr < right_ptr:
                # Swap characters
                string[left_ptr], string[right_ptr] = string[right_ptr], string[left_ptr]
                # Try for next indices
                left_ptr += 1
                right_ptr -= 1

        return "".join(string)


def main():
    s = "ab-cd"
    assert Solution().reverseOnlyLetters(s) == "dc-ba"

    s = "a-bC-dEf-ghIj"
    assert Solution().reverseOnlyLetters(s) == "j-Ih-gfE-dCba"

    s = "Test1ng-Leet=code-Q!"
    assert Solution().reverseOnlyLetters(s) == "Qedo1ct-eeLg=ntse-T!"

    s = "7_28]"
    assert Solution().reverseOnlyLetters(s) == "7_28]"


if __name__ == '__main__':
    main()
