# -*- coding: utf-8 -*-
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(0, force-1)
            forces[i] += force

        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(0, force-1)
            forces[i] -= force

        answer = list()
        for force in forces:
            if force > 0:
                answer.append('R')
            elif force < 0:
                answer.append('L')
            else:
                answer.append('.')

        return ''.join(answer)


def main():
    obj = Solution()
    dominoes = "RR.L"
    assert obj.pushDominoes(dominoes) == "RR.L"
    dominoes = ".L.R...LR..L.."
    assert obj.pushDominoes(dominoes) == "LL.RR.LLRRLL.."


if __name__ == '__main__':
    main()
