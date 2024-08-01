from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([True for d in details if int(d[11:13]) > 60])


def main():
    details = ['7868190130M7522', '5303914400F9211', '9273338290F4010']
    assert Solution().countSeniors(details) == 2

    details = ['1313579440F2036', '2921522980M5644']
    assert Solution().countSeniors(details) == 0


if __name__ == '__main__':
    main()
