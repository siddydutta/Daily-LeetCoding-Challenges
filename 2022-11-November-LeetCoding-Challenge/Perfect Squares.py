class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(n**0.5)+1)]
        queue, next_queue = {n}, set()
        depth = 1

        while queue:
            for node in queue:
                for square in squares:
                    if node == square:
                        return depth
                    if node < square:
                        break
                    next_queue.add(node-square)
            queue = next_queue - queue
            next_queue = set()
            depth += 1


def main():
    n = 12
    assert Solution().numSquares(n) == 3

    n = 13
    assert Solution().numSquares(n) == 2

    n = 7929
    assert Solution().numSquares(n) == 2


if __name__ == '__main__':
    main()
