class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.deque = [None for _ in range(k)]
        self.head = 0
        self.tail = -1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head-1+self.k) % self.k
        self.deque[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail+1) % self.k
        self.deque[self.tail] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head+1) % self.k
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail-1+self.k) % self.k
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k


def main():
    obj = MyCircularDeque(3)
    assert obj.insertLast(1) is True
    assert obj.insertLast(2) is True
    assert obj.insertFront(3) is True
    assert obj.insertFront(4) is False
    assert obj.getRear() == 2
    assert obj.isFull() is True
    assert obj.deleteLast() is True
    assert obj.insertFront(4) is True
    assert obj.getFront() == 4


if __name__ == '__main__':
    main()
