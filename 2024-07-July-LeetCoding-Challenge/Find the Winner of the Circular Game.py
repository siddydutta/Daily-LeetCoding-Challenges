class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        index = 0
        while len(friends) != 1:
            index = index + k - 1
            index = index % n
            friends.pop(index)
            n = n - 1
        return friends[0]


def main():
    n = 5
    k = 2
    assert Solution().findTheWinner(n, k) == 3

    n = 6
    k = 5
    assert Solution().findTheWinner(n, k) == 1


if __name__ == '__main__':
    main()
