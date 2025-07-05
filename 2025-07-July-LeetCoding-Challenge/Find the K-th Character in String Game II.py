class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        k -= 1
        res = 0
        for i, op in enumerate(operations):
            if k & (1 << i):
                res += op
        return chr(ord('a') + res % 26)


def main():
    k = 5
    operations = [0, 0, 0]
    assert Solution().kthCharacter(k, operations) == 'a'

    k = 10
    operations = [0, 1, 0, 1]
    assert Solution().kthCharacter(k, operations) == 'b'


if __name__ == '__main__':
    main()
