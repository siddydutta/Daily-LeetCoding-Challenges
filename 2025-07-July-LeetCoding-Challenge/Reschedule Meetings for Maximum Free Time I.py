class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        gaps = [startTime[0]]  # 0 - first meeting
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i - 1])  # previous meeting - current meeting
        gaps.append(eventTime - endTime[-1])  # last meeting - end

        # sliding window approach -> k+1 gaps
        left, right = 0, 0
        curr_gap, max_gap = 0, 0
        while right < len(gaps):
            curr_gap += gaps[right]
            if right - left > k:
                # sliding window of size k+1
                curr_gap -= gaps[left]
                left += 1
            max_gap = max(max_gap, curr_gap)
            right += 1
        return max_gap


def main():
    eventTime = 5
    k = 1
    startTime = [1, 3]
    endTime = [2, 5]
    assert Solution().maxFreeTime(eventTime, k, startTime, endTime) == 2

    eventTime = 10
    k = 1
    startTime = [0, 2, 9]
    endTime = [1, 4, 10]
    assert Solution().maxFreeTime(eventTime, k, startTime, endTime) == 6

    eventTime = 5
    k = 2
    startTime = [0, 1, 2, 3, 4]
    endTime = [1, 2, 3, 4, 5]
    assert Solution().maxFreeTime(eventTime, k, startTime, endTime) == 0


if __name__ == '__main__':
    main()
