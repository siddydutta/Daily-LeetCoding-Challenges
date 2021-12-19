# -*- coding: utf-8 -*-
class RecursiveSolution:
    def decodeString(self, s: str) -> str:
        ''' Recursive solution. '''
        def build_string(idx: int, k: int = 0, string: str = "") -> str:
            ''' Returns computed subproblem and index till where completed. '''
            while idx < len(s):
                while s[idx].isdigit():
                    # Form multiple, example: 123[abc]
                    k = k*10 + int(s[idx])
                    idx += 1

                if s[idx] == '[':
                    # Calculate substring (sub-problem) within brackets
                    next_string, idx = build_string(idx+1)
                    string += k*next_string  # Add substring result
                    k = int()  # Reset multiple
                elif s[idx] == ']':
                    # Return string and index till where computed
                    return string, idx
                else:
                    # Add individual character to the string
                    string += s[idx]
                idx += 1
            return string, idx

        return build_string(0)[0]


class IterativeSolution:
    def decodeString(self, s: str) -> str:
        ''' Iterative solution using stack. '''
        stack = list()
        string, k = str(), int()

        for ch in s:
            if ch.isdigit():
                k = k*10 + int(ch)
            elif ch == '[':
                stack.append(string)  # Push string until now
                stack.append(k)  # Push multiple
                string, k = str(), int()
            elif ch == ']':
                mul, prev_string = stack.pop(), stack.pop()
                # Pop previous string and multiple with string
                string = prev_string + mul*string
            else:
                string += ch

        return string


def main():
    for obj in [RecursiveSolution(), IterativeSolution()]:
        s = "3[a]2[bc]"
        assert obj.decodeString(s) == "aaabcbc"

        s = "3[a2[c]]"
        assert obj.decodeString(s) == "accaccacc"

        s = "2[abc]3[cd]ef"
        assert obj.decodeString(s) == "abcabccdcdcdef"

        s = "abc3[cd]xyz"
        assert obj.decodeString(s) == "abccdcdcdxyz"


if __name__ == '__main__':
    main()
