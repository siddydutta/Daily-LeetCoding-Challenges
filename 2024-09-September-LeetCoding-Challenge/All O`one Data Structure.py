class Block:
    def __init__(self, count: int = 0):
        self.count = count
        self.keys = set()
        self.before = None
        self.after = None

    def remove(self) -> None:
        self.before.after = self.after
        self.after.before = self.before
        self.before, self.after = None, None

    def add_block(self, block: 'Block') -> None:
        self.after.before = block
        block.after = self.after
        block.before = self
        self.after = block


class AllOne:
    def __init__(self):
        self.head = Block()  # dummy
        self.tail = Block()  # dummy
        self.head.after = self.tail
        self.tail.before = self.head
        self.mapping = dict()

    def inc(self, key: str) -> None:
        # get or create current block
        if key in self.mapping:
            block = self.mapping[key]
            block.keys.remove(key)
        else:
            block = self.head

        # get or create next block
        if block.count+1 != block.after.count:
            new_block = Block(block.count+1)
            block.add_block(new_block)
        else:
            new_block = block.after
        new_block.keys.add(key)
        self.mapping[key] = new_block

        # delete current block if empty
        if not block.keys and block.count != 0:
            block.remove()

    def dec(self, key: str) -> None:
        # get current block
        block = self.mapping.pop(key)
        block.keys.remove(key)

        if block.count != 1:
            # get or create previous block
            if block.count-1 != block.before.count:
                new_block = Block(block.count-1)
                block.before.add_block(new_block)
            else:
                new_block = block.before
            new_block.keys.add(key)
            self.mapping[key] = new_block

        # delete current block if empty
        if not block.keys:
            block.remove()

    def getMaxKey(self) -> str:
        if self.tail.before.count == 0:
            return ''
        return next(iter(self.tail.before.keys))

    def getMinKey(self) -> str:
        if self.head.after.count == 0:
            return ''
        return next(iter(self.head.after.keys))


def main():
    all_one = AllOne()
    all_one.inc('hello')
    all_one.inc('hello')
    assert all_one.getMaxKey() == 'hello'
    assert all_one.getMinKey() == 'hello'
    all_one.inc('leet')
    assert all_one.getMaxKey() == 'hello'
    assert all_one.getMinKey() == 'leet'


if __name__ == '__main__':
    main()
