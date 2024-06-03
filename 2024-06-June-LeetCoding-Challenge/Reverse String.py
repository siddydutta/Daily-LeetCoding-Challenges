from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr1, ptr2 = 0, len(s)-1
        while ptr1 < ptr2:
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            ptr1 += 1
            ptr2 -= 1


def main():
    s = ['h', 'e', 'l', 'l', 'o']
    Solution().reverseString(s)
    assert s == ['o', 'l', 'l', 'e', 'h']

    s = ['H', 'a', 'n', 'n', 'a', 'h']
    Solution().reverseString(s)
    assert s == ['h', 'a', 'n', 'n', 'a', 'H']


if __name__ == '__main__':
    main()
