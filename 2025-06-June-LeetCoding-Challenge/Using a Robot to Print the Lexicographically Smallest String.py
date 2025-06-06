from itertools import accumulate


class Solution:
    def robotWithString(self, s: str) -> str:
        stack, result = [], []
        suffix_min = list(accumulate(reversed(s), min))[::-1]
        for i in range(len(s)):
            while stack and stack[-1] <= suffix_min[i]:
                result.append(stack.pop())
            stack.append(s[i])
        result.extend(reversed(stack))
        return "".join(result)


def main():
    s = 'zza'
    assert Solution().robotWithString(s) == 'azz'

    s = 'bac'
    assert Solution().robotWithString(s) == 'abc'

    s = 'bdda'
    assert Solution().robotWithString(s) == 'addb'


if __name__ == '__main__':
    main()
