# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_key = keysPressed[0]
        max_duration = releaseTimes[0]
        
        for index in range(1, len(keysPressed)):
            key = keysPressed[index]
            duration = releaseTimes[index] - releaseTimes[index-1]
            if duration > max_duration:
                max_key = key
                max_duration = duration
            elif duration == max_duration and key > max_key:
                max_key = key
        return max_key


def main():
    releaseTimes = [9, 29, 49, 50]
    keysPressed = "cbcd"
    assert Solution().slowestKey(releaseTimes, keysPressed) == "c"

    releaseTimes = [12,23,36,46,62]
    keysPressed = "spuda"
    assert Solution().slowestKey(releaseTimes, keysPressed) == "a"


if __name__ == '__main__':
    main()
