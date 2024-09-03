class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ''.join([str(ord(ch)-ord('a')+1) for ch in s])
        for _ in range(k):
            # convert = ''.join(list(str(sum([int(d) for d in convert]))))
            convert = str(sum(list(map(int, convert))))
        return int(convert)


def main():
    s = 'iiii'
    k = 1
    assert Solution().getLucky(s, k) == 36

    s = 'leetcode'
    k = 2
    assert Solution().getLucky(s, k) == 6

    s = 'zbax'
    k = 2
    assert Solution().getLucky(s, k) == 8


if __name__ == '__main__':
    main()
