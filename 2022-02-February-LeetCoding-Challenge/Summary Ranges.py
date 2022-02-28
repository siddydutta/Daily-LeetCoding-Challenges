# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ''' Two pointer based solution. '''
        if len(nums) <= 1:
            return list(map(str, nums))  # Edge case

        ranges = list()
        ptr = start = nums.pop(0)
        while nums:
            end = nums.pop(0)  # Next number from array
            if end - ptr == 1:
                ptr = end  # If consecutive, move pointer
            else:
                if start == ptr:
                    ranges.append(str(start))  # Only one in range
                else:
                    ranges.append(f"{start}->{ptr}")
                ptr = start = end  # Reset start, pointer to next
        # Append last range
        if start == ptr:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{ptr}")
        return ranges


def main():
    nums = [0, 1, 2, 4, 5, 7]
    assert Solution().summaryRanges(nums) == ["0->2", "4->5", "7"]

    nums = [0, 2, 3, 4, 6, 8, 9]
    assert Solution().summaryRanges(nums) == ["0", "2->4", "6", "8->9"]


if __name__ == '__main__':
    main()
