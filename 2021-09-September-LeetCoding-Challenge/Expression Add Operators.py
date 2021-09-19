from typing import List


class Solution:
    ''' Recursive solution using Python's eval. '''
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def recursive(i, s, leading):
            if i >= n:
                if eval(s) == target:
                    ans.append(s)
                return

            if leading != '0':
                recursive(i+1, s+num[i], leading)
            recursive(i+1, s+"+"+num[i], num[i])
            recursive(i+1, s+"-"+num[i], num[i])
            recursive(i+1, s+"*"+num[i], num[i])

        recursive(1, num[0], num[0])
        return ans


def main():
    num = "123"
    target = 6
    assert Solution().addOperators(num, target) == ["1+2+3", "1*2*3"]

    num = "232"
    target = 8
    assert Solution().addOperators(num, target) == ["2+3*2", "2*3+2"]

    num = "105"
    target = 5
    assert Solution().addOperators(num, target) == ["10-5", "1*0+5"]

    num = "00"
    target = 0
    assert Solution().addOperators(num, target) == ["0+0", "0-0", "0*0"]

    num = "3456237490"
    target = 9191
    assert Solution().addOperators(num, target) == []


if __name__ == '__main__':
    main()
