# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def ladderLength(self, begin_word: str, end_word: str,
                     word_list: List[str]) -> int:
        ''' BFS based solution. '''
        words = set(word_list)  # unique set is good enough
        if end_word not in words:
            return 0  # Trivial edge case

        sequence = [begin_word, None]
        count = 1
        n = len(begin_word)  # All words are of the same length

        while sequence[0]:
            while sequence[0]:
                word = sequence.pop(0)
                for pos in range(n):
                    for ch in range(26):
                        # Creates all possible next combinations of word
                        new_word = word[:pos] + chr(ch+97) + word[pos+1:]
                        if new_word in words:
                            sequence.append(new_word)
                            words.remove(new_word)
                            # Check if sequence is complete
                            if new_word == end_word:
                                return count+1
            sequence.pop(0)
            count += 1
            sequence.append(None)
        return 0


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert Solution().ladderLength(beginWord, endWord, wordList) == 5

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot, ""dot", "dog", "lot", "log"]
    assert Solution().ladderLength(beginWord, endWord, wordList) == 0


if __name__ == '__main__':
    main()
