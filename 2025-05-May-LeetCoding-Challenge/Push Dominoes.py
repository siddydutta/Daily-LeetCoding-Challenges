class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # forward pass
        force = 0
        for i in range(n):
            if dominoes[i] == 'L':
                force = 0
            elif dominoes[i] == 'R':
                force = n
            else:
                force = max(0, force - 1)
            forces[i] += force

        # backward pass
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force

        # final state
        result = ''
        for force in forces:
            if force > 0:
                result += 'R'
            elif force < 0:
                result += 'L'
            else:
                result += '.'
        return result


def main():
    dominoes = 'RR.L'
    assert Solution().pushDominoes(dominoes) == 'RR.L'

    dominoes = '.L.R...LR..L..'
    assert Solution().pushDominoes(dominoes) == 'LL.RR.LLRRLL..'


if __name__ == '__main__':
    main()
