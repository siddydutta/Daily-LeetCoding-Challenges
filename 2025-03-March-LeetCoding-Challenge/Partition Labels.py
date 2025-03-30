class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {ch: idx for idx, ch in enumerate(s)}
        result = [0]
        ptr = 0
        while ptr < len(s):
            end = last[s[ptr]]
            while ptr <= end:
                ch = s[ptr]
                end = max(end, last[ch])
                ptr += 1
            result.append(ptr)
        return [result[idx] - result[idx-1] for idx in range(1, len(result))]


def main():
    s = 'ababcbacadefegdehijhklij'
    assert Solution().partitionLabels(s) == [9, 7, 8]

    s = 'eccbbbbdec'
    assert Solution().partitionLabels(s) == [10]


if __name__ == '__main__':
    main()
