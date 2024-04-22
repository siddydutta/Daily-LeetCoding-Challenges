from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if '0000' in visited:
            return -1
        queue = deque(['0000'])
        visited.add('0000')
        turns = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return turns
                for pos in range(4):
                    for delta in (-1, 1):
                        new = list(current)
                        new[pos] = str((int(new[pos]) + delta) % 10)
                        new = ''.join(new)
                        if new not in visited:
                            queue.append(new)
                            visited.add(new)
            turns += 1
        return -1


def main():
    deadends = ['0201', '0101', '0102', '1212', '2002']
    target = '0202'
    assert Solution().openLock(deadends, target) == 6

    deadends = ['8888']
    target = '0009'
    assert Solution().openLock(deadends, target) == 1

    deadends = ['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888']
    target = '8888'
    assert Solution().openLock(deadends, target) == -1


if __name__ == '__main__':
    main()
