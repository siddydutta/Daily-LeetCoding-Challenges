from collections import deque


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        next_map = {'a': 'bc', 'b': 'ac', 'c': 'ab'}
        queue = deque(next_map.keys())
        while len(queue[0]) != n:
            u = queue.popleft()
            for v in next_map[u[-1]]:
                queue.append(u + v)
        return queue[k-1] if len(queue) >= k else ''


def main():
    n = 1
    k = 3
    assert Solution().getHappyString(n, k) == 'c'

    n = 1
    k = 4
    assert Solution().getHappyString(n, k) == ''

    n = 3
    k = 9
    assert Solution().getHappyString(n, k) == 'cab'


if __name__ == '__main__':
    main()
