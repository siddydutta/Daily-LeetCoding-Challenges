# -*- coding: utf-8 -*-
class Element:
    ''' Stack element maintaining value and minimum value so far. '''
    def __init__(self, val, min_val):
        self.val = val
        self.min_val = min_val


class MinStack:
    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        if self.stack:
            current_min = min(self.getMin(), val)
            self.stack.append(Element(val, current_min))
        else:
            self.stack.append(Element(val, val))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min_val


def main():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    assert min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2


if __name__ == '__main__':
    main()
