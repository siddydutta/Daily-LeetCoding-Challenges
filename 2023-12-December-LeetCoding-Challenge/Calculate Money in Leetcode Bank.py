class Solution:
    def totalMoney(self, n: int) -> int:
        last_monday = 0
        curr_day = 0
        money = []
        while n != 0:
            if curr_day == 0:
                money.append(last_monday+1)
                last_monday += 1
            else:
                money.append(money[-1]+1)
            curr_day = (curr_day + 1) % 7
            n -= 1
        return sum(money)


def main():
    n = 4
    assert Solution().totalMoney(n) == 10

    n = 10
    assert Solution().totalMoney(n) == 37

    n = 20
    assert Solution().totalMoney(n) == 96


if __name__ == '__main__':
    main()
