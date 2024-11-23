from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            empty = len(row) - 1
            for i in range(len(row)-1, -1, -1):
                if row[i] == '*':
                    empty = i - 1
                elif row[i] == '#':
                    row[empty], row[i] = row[i], row[empty]
                    empty -= 1

        # rows, cols = len(box), len(box[0])
        # result = [[None]*rows for _ in range(cols)]
        # for i, j in product(range(rows), range(cols)):
        #     result[j][rows-1-i] = box[i][j]
        # return result
        return list(map(list, zip(*reversed(box))))


def main():
    box = [['#', '.', '#']]
    assert Solution().rotateTheBox(box) == [['.'],
                                            ['#'],
                                            ['#']]

    box = [['#', '.', '*', '.'],
           ['#', '#', '*', '.']]
    assert Solution().rotateTheBox(box) == [['#', '.'],
                                            ['#', '#'],
                                            ['*', '*'],
                                            ['.', '.']]

    box = [['#', '#', '*', '.', '*', '.'],
           ['#', '#', '#', '*', '.', '.'],
           ['#', '#', '#', '.', '#', '.']]
    assert Solution().rotateTheBox(box) == [['.', '#', '#'],
                                            ['.', '#', '#'],
                                            ['#', '#', '*'],
                                            ['#', '*', '.'],
                                            ['#', '.', '*'],
                                            ['#', '.', '.']]


if __name__ == '__main__':
    main()
