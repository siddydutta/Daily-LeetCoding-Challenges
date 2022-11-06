class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            # can be bubble sorted
            return "".join(sorted(s))
        min_str = s
        for _ in range(len(s)-1):
            # rotate string one letter at a time
            s = s[1:] + s[0]
            min_str = min(min_str, s)
        return min_str


def main():
    s = "cba"
    k = 1
    assert Solution().orderlyQueue(s, k) == "acb"

    s = "baaca"
    k = 3
    assert Solution().orderlyQueue(s, k) == "aaabc"


if __name__ == '__main__':
    main()
