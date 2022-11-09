class StockSpanner:
    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


def main():
    stockSpanner: StockSpanner = StockSpanner()
    assert stockSpanner.next(100) == 1
    assert stockSpanner.next(80) == 1
    assert stockSpanner.next(60) == 1
    assert stockSpanner.next(70) == 2
    assert stockSpanner.next(60) == 1
    assert stockSpanner.next(75) == 4
    assert stockSpanner.next(85) == 6


if __name__ == '__main__':
    main()
