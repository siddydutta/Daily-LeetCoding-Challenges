class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def recursive(idx: int = int(), strs: set = set()) -> None:
            if idx == len(s):
                return len(strs)
            max_splits = 0
            for i in range(idx+1, len(s)+1):
                sub = s[idx:i]
                if sub not in strs:
                    strs.add(sub)
                    max_splits = max(max_splits, recursive(i, strs))
                    strs.remove(sub)
            return max_splits
        return recursive()


def main():
    s = 'ababccc'
    assert Solution().maxUniqueSplit(s) == 5

    s = 'aba'
    assert Solution().maxUniqueSplit(s) == 2

    s = 'aa'
    assert Solution().maxUniqueSplit(s) == 1


if __name__ == '__main__':
    main()
