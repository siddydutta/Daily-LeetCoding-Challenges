class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_brackets, unlocked = [], []
        for i, b in enumerate(s):
            if locked[i] == '0':
                unlocked.append(i)
            elif b == '(':
                open_brackets.append(i)
            else:
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while open_brackets and unlocked:
            if open_brackets[-1] < unlocked[-1]:
                open_brackets.pop()
                unlocked.pop()
            else:
                break
        return not open_brackets


def main():
    s = '))()))'
    locked = '010100'
    assert Solution().canBeValid(s, locked) is True

    s = '()()'
    locked = '0000'
    assert Solution().canBeValid(s, locked) is True

    s = ')'
    locked = '0'
    assert Solution().canBeValid(s, locked) is False


if __name__ == '__main__':
    main()
