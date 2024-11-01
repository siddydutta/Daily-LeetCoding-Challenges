class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_char, curr_count = None, 0
        result = ''
        for ch in s:
            if ch == prev_char:
                curr_count += 1
            else:
                curr_count = 1
            if curr_count < 3:
                result += ch
            prev_char = ch
        return result


def main():
    s = 'leeetcode'
    assert Solution().makeFancyString(s) == 'leetcode'

    s = 'aaabaaaa'
    assert Solution().makeFancyString(s) == 'aabaa'

    s = 'aab'
    assert Solution().makeFancyString(s) == 'aab'


if __name__ == '__main__':
    main()
