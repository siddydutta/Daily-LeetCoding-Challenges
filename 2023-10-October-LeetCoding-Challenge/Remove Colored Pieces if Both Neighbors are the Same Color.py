class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # count consecutive pieces
        alice, bob = list(), list()
        current = colors[0]
        index, count = 1, 1
        while index < len(colors):
            if colors[index] == current:
                count += 1
            else:
                alice.append(count) if current == 'A' else bob.append(count)
                current = colors[index]
                count = 1
            index += 1
        alice.append(count) if current == 'A' else bob.append(count)
        if current == 'A':
            alice.append(count)

        # play optimally
        while True:
            while alice and alice[0] < 3:
                alice.pop(0)
            alice_move = False
            if alice:
                alice[0] -= 1
                alice_move = True
            if not alice_move:
                return False  # bob wins
            while bob and bob[0] < 3:
                bob.pop(0)
            bob_move = False
            if bob:
                bob[0] -= 1
                bob_move = True
            if not bob_move:
                return True  # alice wins


def main():
    colors = "AAABABB"
    assert Solution().winnerOfGame(colors)

    colors = "AA"
    assert not Solution().winnerOfGame(colors)

    colors = "ABBBBBBBAAA"
    assert not Solution().winnerOfGame(colors)


if __name__ == '__main__':
    main()
