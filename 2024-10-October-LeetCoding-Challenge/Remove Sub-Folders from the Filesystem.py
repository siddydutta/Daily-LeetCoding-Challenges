from typing import Generator, List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path: str) -> None:
        node = self.root
        for folder in path.split('/')[1:]:
            node = node.children.setdefault(folder, TrieNode())
            if node.is_end:
                return
        node.is_end = True
        node.children.clear()

    def collect(self, node: TrieNode, path: str = '') -> Generator[str, None, None]:
        if node.is_end:
            yield path
        for folder, child in node.children.items():
            yield from self.collect(child, f'{path}/{folder}')


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for path in folder:
            trie.insert(path)
        return list(trie.collect(trie.root))


def main():
    folder = ['/a', '/a/b', '/c/d', '/c/d/e', '/c/f']
    assert Solution().removeSubfolders(folder) == ['/a', '/c/d', '/c/f']

    folder = ['/a', '/a/b/c', '/a/b/d']
    assert Solution().removeSubfolders(folder) == ['/a']

    folder = ['/a/b/c', '/a/b/ca', '/a/b/d']
    assert Solution().removeSubfolders(folder) == ['/a/b/c', '/a/b/ca', '/a/b/d']


if __name__ == '__main__':
    main()
