class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result, stack = [], []
        for idx in range(n+1):
            stack.append(str(idx+1))
            if idx == n or pattern[idx] == 'I':
                while stack:
                    result.append(stack.pop())
        return ''.join(result)


def main():
    pattern = 'IIIDIDDD'
    assert Solution().smallestNumber(pattern) == '123549876'

    pattern = 'DDD'
    assert Solution().smallestNumber(pattern) == '4321'


if __name__ == '__main__':
    main()
