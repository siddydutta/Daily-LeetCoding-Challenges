from collections import deque
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # order invariance: flip the bit at the start of the window
        # parity invariance: flip the bit at the start of the window
        #                    if the window has been flipped odd times
        flip_queue = deque()  # store flip states of window
        flipped = False  # current flip state
        result = 0

        for i, num in enumerate(nums):
            # update the flip state after extending window
            if i >= k and flip_queue:
                if flip_queue.popleft() is True:
                    # toggle the flip state if flip
                    flipped = not flipped

            # check if the current bit needs to be flipped
            if (not flipped and num == 0) or (flipped and num == 1):
                if i+k > len(nums):
                    # flip is not possible
                    return -1

                flip_queue.append(True)
                flipped = not flipped
                result += 1
            else:
                flip_queue.append(False)

        return result


def main():
    nums = [0, 1, 0]
    k = 1
    assert Solution().minKBitFlips(nums, k) == 2

    nums = [1, 1, 0]
    k = 2
    assert Solution().minKBitFlips(nums, k) == -1

    nums = [0, 0, 0, 1, 0, 1, 1, 0]
    k = 3
    assert Solution().minKBitFlips(nums, k) == 3


if __name__ == '__main__':
    main()
