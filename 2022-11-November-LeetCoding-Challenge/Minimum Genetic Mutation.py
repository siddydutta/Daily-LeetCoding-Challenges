from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank, visited = set(bank), set()
        queue = [(start, 0)]

        while queue:
            seq, count = queue.pop(0)
            if seq == end:
                return count

            for ch in "ACGT":
                # try to create all possible paths
                for index in range(len(seq)):
                    new_seq = seq[:index] + ch + seq[index+1:]
                    if new_seq not in visited and new_seq in bank:
                        queue.append((new_seq, count+1))
                        visited.add(new_seq)
        return -1


def main():
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    assert Solution().minMutation(start, end, bank) == 1

    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    assert Solution().minMutation(start, end, bank) == 2

    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    assert Solution().minMutation(start, end, bank) == 3


if __name__ == '__main__':
    main()
