from random import choice


class RandomizedSet:
    def __init__(self):
        self.values = list()
        self.index = dict()

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.values.append(val)
        self.index[val] = len(self.values)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        idx = self.index[val]
        # move last value to idx
        last_value = self.values[-1]
        self.values[idx] = last_value
        self.index[last_value] = idx
        del self.index[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.values)


def main():
    randomizedSet = RandomizedSet()
    assert randomizedSet.insert(1)
    assert not randomizedSet.remove(2)
    assert randomizedSet.insert(2)
    assert randomizedSet.getRandom() in {1, 2}
    assert randomizedSet.remove(1)
    assert not randomizedSet.insert(2)
    assert randomizedSet.getRandom() == 2


if __name__ == '__main__':
    main()
