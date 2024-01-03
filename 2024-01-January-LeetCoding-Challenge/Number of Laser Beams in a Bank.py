from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = map(lambda row: row.count('1'), bank)
        bank = list(filter(lambda count: count != 0, bank))
        return sum([r1*r2 for r1, r2 in zip(bank, bank[1:])])


def main():
    bank = ['011001', '000000', '010100', '001000']
    assert Solution().numberOfBeams(bank) == 8

    bank = ['000', '111', '000']
    assert Solution().numberOfBeams(bank) == 0


if __name__ == '__main__':
    main()
