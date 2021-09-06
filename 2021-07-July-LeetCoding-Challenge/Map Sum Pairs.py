# -*- coding: utf-8 -*-
class MapSum:
    ''' Naive Solution. '''
    def __init__(self):
        self.map = dict()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        s = 0
        for key, value in self.map.items():
            if key.startswith(prefix):
                s += value
        return s


def main():
    mapSum = MapSum()
    mapSum.insert("apple", 3)
    assert mapSum.sum("ap") == 3
    mapSum.insert("app", 2)
    assert mapSum.sum("ap") == 5


if __name__ == '__main__':
    main()
