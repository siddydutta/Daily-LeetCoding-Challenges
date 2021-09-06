# -*- coding: utf-8 -*-
class SimpleRecursiveSolution:
    '''
    Follows a three pointer approach, matching s3 characters with either s1
    or s2 and recursively solving when s1 and s2 characters are the same.
    Time Complexity: O(2^(|s1|+|s2|)) and hence leads to a TLE.
    '''
    def solver(self, s1: str, s2: str, s3: str,
               p1: int, p2: int, p3: int) -> bool:
        # Base Condition -> All pointers have reached the end
        if p1 == len(s1) and p2 == len(s2) and p3 == len(s3):
            return True

        # s3 char is same as s1 and s2, branch to check both str possibilities
        if p1 < len(s1) and p2 < len(s2) and s3[p3] == s1[p1] == s2[p2]:
            return self.solver(s1, s2, s3, p1+1, p2, p3+1) or \
                    self.solver(s1, s2, s3, p1, p2+1, p3+1)
        # s3 char is same as s1 char only
        elif p1 < len(s1) and s1[p1] == s3[p3]:
            return self.solver(s1, s2, s3, p1+1, p2, p3+1)
        # s3 char is same as s2 char only
        elif p2 < len(s2) and s2[p2] == s3[p3]:
            return self.solver(s1, s2, s3, p1, p2+1, p3+1)
        # No Match
        else:
            return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Base Cases
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        return self.solver(s1, s2, s3, 0, 0, 0)


class Solution:
    '''
    Similar approach to recursive solution but introduces caching ie.
    memoization to prevent unecessary recomputations.
    The map's key is of the format pointer1-pointer2-pointer3.
    '''
    def __init__(self):
        self.cache = dict()

    def solver(self, s1: str, s2: str, s3: str,
               p1: int, p2: int, p3: int) -> bool:
        # Base Condition -> All pointers have reached the end
        if p1 == len(s1) and p2 == len(s2) and p3 == len(s3):
            return True

        # Check Cache
        key = str(p1) + '-' + str(p2) + '-' + str(p3)
        if key in self.cache:
            return self.cache.get(key)

        # Cases where end of either string has been reached
        if p1 == len(s1):
            result = s2[p2:] == s3[p3:]
            self.cache[key] = result
            return result
        if p2 == len(s2):
            result = s1[p1:] == s3[p3:]
            self.cache[key] = result
            return result

        res1, res2 = False, False
        if s1[p1] == s3[p3]:
            res1 = self.solver(s1, s2, s3, p1+1, p2, p3+1)
        if s2[p2] == s3[p3]:
            res2 = self.solver(s1, s2, s3, p1, p2+1, p3+1)
        result = res1 or res2
        self.cache[key] = result
        return result

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Base Cases
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        return self.solver(s1, s2, s3, 0, 0, 0)


if __name__ == '__main__':
    obj = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    assert obj.isInterleave(s1, s2, s3)

    obj = Solution()
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbb" + \
        "ababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaa" + \
        "baabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaab" + \
        "baaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabb" + \
        "abbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbabab" + \
        "babbabbab"
    assert not obj.isInterleave(s1, s2, s3)
