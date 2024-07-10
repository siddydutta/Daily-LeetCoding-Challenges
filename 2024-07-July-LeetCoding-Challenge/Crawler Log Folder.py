from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = list()
        for log in logs:
            if log == '../':
                if path:
                    path.pop()
            elif log == './':
                continue
            else:
                path.append(log)
        return len(path)


def main():
    logs = ['d1/', 'd2/', '../', 'd21/', './']
    assert Solution().minOperations(logs) == 2

    logs = ['d1/', 'd2/', './', 'd3/', '../', 'd31/']
    assert Solution().minOperations(logs) == 3

    logs = ['d1/', '../', '../', '../']
    assert Solution().minOperations(logs) == 0


if __name__ == '__main__':
    main()
