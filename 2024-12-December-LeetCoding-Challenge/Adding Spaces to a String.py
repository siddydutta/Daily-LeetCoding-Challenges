from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        ptr = 0
        for i in range(len(s)):
            if ptr < len(spaces) and i == spaces[ptr]:
                res += ' '
                ptr += 1
            res += s[i]
        return res


def main():
    s = 'LeetcodeHelpsMeLearn'
    spaces = [8, 13, 15]
    assert Solution().addSpaces(s, spaces) == 'Leetcode Helps Me Learn'

    s = 'icodeinpython'
    spaces = [1, 5, 7, 9]
    assert Solution().addSpaces(s, spaces) == 'i code in py thon'

    s = 'spacing'
    spaces = [0, 1, 2, 3, 4, 5, 6]
    assert Solution().addSpaces(s, spaces) == ' s p a c i n g'


if __name__ == '__main__':
    main()
