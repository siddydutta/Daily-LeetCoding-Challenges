from collections import Counter
from heapq import heapify, heappop, heappush
from typing import List, Optional, Tuple


class Solution:
    def __heappop(self, heap: List[int]) -> Tuple[Optional[str], int]:
        if len(heap) == 0:
            return (None, 0)
        asc, count = heappop(heap)
        ch = chr(-asc)
        return (ch, count)

    def __heappush(self, heap: List[int], ch: str, count: int):
        if count == 0:
            return
        entry = (-ord(ch), count)
        heappush(heap, entry)

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [(-ord(ch), count) for ch, count in Counter(s).items()]
        heapify(freq)
        string = ''
        while freq:
            curr_ch, curr_count = self.__heappop(freq)
            if string and string[-1] == curr_ch:
                next_ch, next_count = self.__heappop(freq)
                if next_ch is None and next_count == 0:
                    break
                string += next_ch
                self.__heappush(freq, next_ch, next_count-1)
                self.__heappush(freq, curr_ch, curr_count)
            else:
                repeat = min(curr_count, repeatLimit)
                string += (curr_ch * repeat)
                self.__heappush(freq, curr_ch, curr_count-repeat)
        return string


def main():
    s = 'cczazcc'
    repeatLimit = 3
    assert Solution().repeatLimitedString(s, repeatLimit) == 'zzcccac'

    s = 'aababab'
    repeatLimit = 2
    assert Solution().repeatLimitedString(s, repeatLimit) == 'bbabaa'


if __name__ == '__main__':
    main()
