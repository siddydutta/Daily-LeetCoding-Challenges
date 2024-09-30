class CustomStack:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.stack = list()

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


def main():
    stk = CustomStack(3)
    stk.push(1)
    stk.push(2)
    assert stk.pop() == 2
    stk.push(2)
    stk.push(3)
    stk.push(4)
    stk.increment(5, 100)
    stk.increment(2, 100)
    assert stk.pop() == 103
    assert stk.pop() == 202
    assert stk.pop() == 201
    assert stk.pop() == -1


if __name__ == '__main__':
    main()
