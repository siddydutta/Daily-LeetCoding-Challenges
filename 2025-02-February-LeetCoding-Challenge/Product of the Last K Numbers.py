class ProductOfNumbers:
    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return 0
        return self.products[-1] // self.products[-k-1]


def main():
    product_of_numbers = ProductOfNumbers()
    product_of_numbers.add(3)
    product_of_numbers.add(0)
    product_of_numbers.add(2)
    product_of_numbers.add(5)
    product_of_numbers.add(4)
    assert product_of_numbers.getProduct(2) == 20
    assert product_of_numbers.getProduct(3) == 40
    assert product_of_numbers.getProduct(4) == 0
    product_of_numbers.add(8)
    assert product_of_numbers.getProduct(2) == 32


if __name__ == '__main__':
    main()
