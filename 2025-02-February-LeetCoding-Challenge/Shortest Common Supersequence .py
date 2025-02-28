class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        prev_row = [str2[:col] for col in range(l2+1)]
        for row in range(1, l1+1):
            curr_row = [str1[:row]] + ([None]*l2)
            for col in range(1, l2+1):
                if str1[row-1] == str2[col-1]:
                    curr_row[col] = prev_row[col-1] + str1[row-1]
                else:
                    p_s1 = prev_row[col]
                    p_s2 = curr_row[col-1]
                    curr_row[col] = (p_s1 + str1[row-1]
                                     if len(p_s1) < len(p_s2)
                                     else p_s2 + str2[col-1])
            prev_row = curr_row
        return prev_row[l2]


def main():
    str1 = 'abac'
    str2 = 'cab'
    assert Solution().shortestCommonSupersequence(str1, str2) == 'cabac'

    str1 = 'bbbaaaba'
    str2 = 'bbababbb'
    assert Solution().shortestCommonSupersequence(str1, str2) == 'bbbaaababbb'


if __name__ == '__main__':
    main()
