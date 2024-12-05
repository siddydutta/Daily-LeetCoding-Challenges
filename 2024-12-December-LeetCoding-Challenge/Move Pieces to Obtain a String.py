class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        ptr1, ptr2 = 0, 0

        while ptr1 < n or ptr2 < n:
            while ptr1 < n and start[ptr1] == '_':
                ptr1 += 1
            while ptr2 < n and target[ptr2] == '_':
                ptr2 += 1
            if n == ptr1 or n == ptr2:
                return ptr1 == ptr2 == n
            if start[ptr1] != target[ptr2]:
                return False
            if start[ptr1] == 'L':
                if ptr1 < ptr2:
                    return False
            else:
                if ptr1 > ptr2:
                    return False
            ptr1 += 1
            ptr2 += 1

        return True


def main():
    start = '_L__R__R_'
    target = '_L__R__R_'
    assert Solution().canChange(start, target) is True

    start = 'R_L_'
    target = '__LR'
    assert Solution().canChange(start, target) is False

    start = '_R'
    target = 'R_'
    assert Solution().canChange(start, target) is False


if __name__ == '__main__':
    main()
