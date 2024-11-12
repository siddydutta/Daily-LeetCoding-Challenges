from bisect import bisect_right
from typing import List


class Solution:
    def maximumBeauty(
            self, items: List[List[int]], queries: List[int]
    ) -> List[int]:
        # sort items by price, then reverse beauty
        items.sort(key=lambda i: (i[0], -i[1]))
        # max accumulate beauty
        max_beauty = items[0][1]
        for item in items[1:]:
            max_beauty = max(max_beauty, item[1])
            item[1] = max_beauty
        # extract prices for bisect
        prices = [item[0] for item in items]
        # most beautiful item for each query
        answer = []
        for query in queries:
            idx = bisect_right(prices, query)
            if idx > 0:
                answer.append(items[idx-1][1])
            else:
                answer.append(0)
        return answer


def main():
    items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
    queries = [1, 2, 3, 4, 5, 6]
    assert Solution().maximumBeauty(items, queries) == [2, 4, 5, 5, 6, 6]

    items = [[1, 2], [1, 2], [1, 3], [1, 4]]
    queries = [1]
    assert Solution().maximumBeauty(items, queries) == [4]

    items = [[10, 1000]]
    queries = [5]
    assert Solution().maximumBeauty(items, queries) == [0]


if __name__ == '__main__':
    main()
