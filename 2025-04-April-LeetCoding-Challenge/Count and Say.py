from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n - 1):
            new_result = ''
            for digit, occs in groupby(result):
                new_result += str(len(list(occs))) + digit
            result = new_result
        return result


def main():
    n = 4
    assert Solution().countAndSay(n) == '1211'

    n = 1
    assert Solution().countAndSay(n) == '1'


if __name__ == '__main__':
    main()
