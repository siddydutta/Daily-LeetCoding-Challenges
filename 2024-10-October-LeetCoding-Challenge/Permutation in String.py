class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            # permutation cannot exist in smaller string
            return False

        s1_c, s2_c = [0]*26, [0]*26
        for i in range(n1):
            # store frequency of characters
            s1_c[ord(s1[i])-97] += 1
            s2_c[ord(s2[i])-97] += 1

        for i in range(n1, n2):
            if s1_c == s2_c:
                # check for initial substring
                return True
            # slide window
            s2_c[ord(s2[i-n1])-97] -= 1
            s2_c[ord(s2[i])-97] += 1
        # check for last substring
        return s1_c == s2_c


def main():
    s1 = 'ab'
    s2 = 'eidbaooo'
    assert Solution().checkInclusion(s1, s2) is True

    s1 = 'ab'
    s2 = 'eidboaoo'
    assert Solution().checkInclusion(s1, s2) is False


if __name__ == '__main__':
    main()
