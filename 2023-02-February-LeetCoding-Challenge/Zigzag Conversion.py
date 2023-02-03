# -*- coding: utf-8 -*-
class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        rows = ["" for _ in range(num_rows)]
        ptr, counter = 0, 0

        while ptr < len(s):
            if counter == num_rows:
                counter -= 1
                while counter > 1 and ptr < len(s):
                    rows[counter-1] += s[ptr]
                    ptr += 1
                    counter -= 1
                counter = 0
            else:
                rows[counter] += s[ptr]
                ptr += 1
                counter += 1

        return "".join(rows)


def main():
    s = "PAYPALISHIRING"
    num_rows = 3
    assert Solution().convert(s, num_rows) == "PAHNAPLSIIGYIR"

    s = "PAYPALISHIRING"
    num_rows = 4
    assert Solution().convert(s, num_rows) == "PINALSIGYAHRPI"

    s = "A"
    num_rows = 1
    assert Solution().convert(s, num_rows) == "A"


if __name__ == '__main__':
    main()
