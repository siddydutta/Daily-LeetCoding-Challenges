class Solution:
    def minOperations(self, s: str) -> int:
        count1, count2 = 0, 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    count1 += 1
                else:
                    count2 += 1
            else:
                if s[i] != '1':
                    count1 += 1
                else:
                    count2 += 1
        return min(count1, count2)


def main():
    s = '0100'
    assert Solution().minOperations(s) == 1

    s = '10'
    assert Solution().minOperations(s) == 0

    s = '1111'
    assert Solution().minOperations(s) == 2


if __name__ == '__main__':
    main()
