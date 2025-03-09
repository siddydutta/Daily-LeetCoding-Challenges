class Solution:
    def numberOfAlternatingGroups(self, colours: list[int], k: int) -> int:
        colours.extend(colours[:(k-1)])
        ptr1, result = 0, 0
        for ptr2 in range(1, len(colours)):
            if colours[ptr2] == colours[ptr2-1]:
                ptr1 = ptr2
            if ptr2 - ptr1 + 1 >= k:
                result += 1
        return result


def main():
    colours = [0, 1, 0, 1, 0]
    k = 3
    assert Solution().numberOfAlternatingGroups(colours, k) == 3

    colours = [0, 1, 0, 0, 1, 0, 1]
    k = 6
    assert Solution().numberOfAlternatingGroups(colours, k) == 2

    colours = [1, 1, 0, 1]
    k = 4
    assert Solution().numberOfAlternatingGroups(colours, k) == 0


if __name__ == '__main__':
    main()
