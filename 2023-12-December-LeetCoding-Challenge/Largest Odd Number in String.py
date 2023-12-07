class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ''


def main():
    num = "52"
    assert Solution().largestOddNumber(num) == '5'

    num = "4206"
    assert Solution().largestOddNumber(num) == ''

    num = "35427"
    assert Solution().largestOddNumber(num) == '35427'


if __name__ == '__main__':
    main()
