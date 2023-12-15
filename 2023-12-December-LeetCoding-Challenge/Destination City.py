from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out_degree_nodes = {source for source, _ in paths}
        for _, destination in paths:
            if destination not in out_degree_nodes:
                return destination


def main():
    paths = [['London', 'New York'],
             ['New York', 'Lima'],
             ['Lima', 'Sao Paulo']]
    assert Solution().destCity(paths) == 'Sao Paulo'

    paths = [['B', 'C'],
             ['D', 'B'],
             ['C', 'A']]
    assert Solution().destCity(paths) == 'A'


if __name__ == '__main__':
    main()
