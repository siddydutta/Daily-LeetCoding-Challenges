class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch_map, ch2_set = dict(), set()
        for ch1, ch2 in zip(s, t):
            if ch1 in ch_map:
                if ch_map[ch1] != ch2:
                    return False
            else:
                if ch2 in ch2_set:
                    return False
                ch_map[ch1] = ch2
                ch2_set.add(ch2)
        return True


def main():
    s, t = 'egg', 'add'
    assert Solution().isIsomorphic(s, t)

    s, t = 'foo', 'bar'
    assert not Solution().isIsomorphic(s, t)

    s, t, = 'paper', 'title'
    assert Solution().isIsomorphic(s, t)


if __name__ == '__main__':
    main()
