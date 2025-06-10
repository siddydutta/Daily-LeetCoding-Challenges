class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        numbers = []

        def dfs(number: int) -> None:
            if number > n:
                return
            nonlocal numbers
            numbers.append(number)
            for digit in range(10):
                num = number * 10 + digit
                if num > n:
                    continue
                dfs(num)

        for i in range(1, 10):
            dfs(i)
        return numbers


def main():
    n = 13
    ans = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Solution().lexicalOrder(n) == ans

    n = 2
    assert Solution().lexicalOrder(n) == [1, 2]


if __name__ == '__main__':
    main()
