from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        translation = str.maketrans(''.join(map(str, range(10))),
                                    ''.join(map(str, mapping)))
        return sorted(nums, key=lambda n: int(str(n).translate(translation)))


def main():
    mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    nums = [991, 338, 38]
    assert Solution().sortJumbled(mapping, nums) == [338, 38, 991]

    mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = [789, 456, 123]
    assert Solution().sortJumbled(mapping, nums) == [123, 456, 789]


if __name__ == '__main__':
    main()
