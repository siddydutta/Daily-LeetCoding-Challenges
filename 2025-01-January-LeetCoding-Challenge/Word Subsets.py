from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        req_freq = defaultdict(int)
        for word in words2:
            for ch, count in Counter(word).items():
                req_freq[ch] = max(req_freq[ch], count)

        result = []
        for word in words1:
            freq = Counter(word)
            for ch, count in req_freq.items():
                if freq[ch] < count:
                    break
            else:
                # for ... else instead of using a flag
                result.append(word)
        return result


def main():
    words1 = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
    words2 = ['e', 'o']
    assert Solution().wordSubsets(words1, words2) == ['facebook', 'google', 'leetcode']

    words1 = ['amazon', 'apple', 'facebook', 'google', 'leetcode']
    words2 = ['l', 'e']
    assert Solution().wordSubsets(words1, words2) == ['apple', 'google', 'leetcode']


if __name__ == '__main__':
    main()
