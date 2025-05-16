class Solution:
    def __is_eligible(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        flag = False
        for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                if flag is True:
                    # hamming distance > 1
                    return False
                flag = True
        # hamming distance == 1
        return flag

    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        n = len(words)
        dp, parent = [1] * n, [-1] * n
        max_len = 0

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and \
                    self.__is_eligible(words[i], words[j]) and \
                        dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            max_len = max(max_len, dp[i])

        result = []
        for i in range(n):
            if dp[i] == max_len:
                while i != -1:
                    result.append(words[i])
                    i = parent[i]
                break
        return list(reversed(result))


def main():
    words = ['bab', 'dab', 'cab']
    groups = [1, 2, 2]
    assert Solution().getWordsInLongestSubsequence(words, groups) == ['bab', 'dab']

    words = ['a', 'b', 'c', 'd']
    groups = [1, 2, 3, 4]
    assert Solution().getWordsInLongestSubsequence(words, groups) == ['a', 'b', 'c', 'd']


if __name__ == '__main__':
    main()
