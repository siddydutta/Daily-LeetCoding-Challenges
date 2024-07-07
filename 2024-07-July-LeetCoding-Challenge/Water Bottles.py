class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        drinks = 0
        empty_bottles = 0
        while num_bottles > 0:
            drinks += num_bottles
            empty_bottles += num_bottles
            num_bottles, empty_bottles = divmod(empty_bottles, num_exchange)
        return drinks


def main():
    num_bottles = 9
    num_exchange = 3
    assert Solution().numWaterBottles(num_bottles, num_exchange) == 13

    num_bottles = 15
    num_exchange = 4
    assert Solution().numWaterBottles(num_bottles, num_exchange) == 19


if __name__ == '__main__':
    main()
