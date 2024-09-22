class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix: int) -> int:
            # counts number of nodes in subtree with root = prefix
            current = prefix
            next_prefix = prefix + 1
            steps = 0
            while current <= n:
                steps += min(n+1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps

        current = 1
        k -= 1
        while k > 0:
            steps = count_steps(current)
            if steps <= k:
                # include entire subtree
                k -= steps
                current += 1
            else:
                # explore subtree
                k -= 1
                current *= 10
        return current


def main():
    n = 13
    k = 2
    assert Solution().findKthNumber(n, k) == 10

    n = 1
    k = 1
    assert Solution().findKthNumber(n, k) == 1


if __name__ == '__main__':
    main()
