from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # return not reduce(xor, derived)
        return not sum(derived) & 1


def main():
    derived = [1, 1, 0]
    assert Solution().doesValidArrayExist(derived) is True

    derived = [1, 1]
    assert Solution().doesValidArrayExist(derived) is True

    derived = [1, 0]
    assert Solution().doesValidArrayExist(derived) is False


if __name__ == '__main__':
    main()
