class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        indices = [[] for _ in range(26)]  # indices of each char
        keep = [True] * n  # flag to keep index in result

        for i in range(n):
            if s[i] == '*':
                keep[i] = False  # remove *
                # find first (smallest) char's latest index
                for j in range(26):
                    if indices[j]:
                        keep[indices[j].pop()] = False
                        break
            else:
                # append index of current char
                indices[ord(s[i]) - ord('a')].append(i)

        return ''.join(s[i] for i in range(n) if keep[i])


def main():
    s = 'aaba*'
    assert Solution().clearStars(s) == 'aab'

    s = 'abc'
    assert Solution().clearStars(s) == 'abc'


if __name__ == '__main__':
    main()
