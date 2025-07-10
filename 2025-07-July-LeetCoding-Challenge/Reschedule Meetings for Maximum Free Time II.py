class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        gaps = [startTime[0]]  # 0 - first meeting
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i - 1])  # previous meeting - current meeting
        gaps.append(eventTime - endTime[-1])  # last meeting - end

        # compute max suffix array
        max_right_gap = [0] * len(gaps)
        for i in range(len(gaps) - 2, -1, -1):
            max_right_gap[i] = max(max_right_gap[i + 1], gaps[i + 1])

        # compute max prefix
        # compute largest possible gap by removing current meeting (if possible)
        max_free_time, max_left_gap = 0, 0
        for i in range(1, len(gaps)):
            curr_meeting = endTime[i - 1] - startTime[i - 1]
            if curr_meeting <= max(max_left_gap, max_right_gap[i]):
                max_free_time = max(max_free_time, gaps[i - 1] + gaps[i] + curr_meeting)
            max_free_time = max(max_free_time, gaps[i - 1] + gaps[i])
            max_left_gap = max(max_left_gap, gaps[i - 1])
        return max_free_time


def main():
    eventTime = 5
    startTime = [1, 3]
    endTime = [2, 5]
    assert Solution().maxFreeTime(eventTime, startTime, endTime) == 2

    eventTime = 10
    startTime = [0, 7, 9]
    endTime = [1, 8, 10]
    assert Solution().maxFreeTime(eventTime, startTime, endTime) == 7

    eventTime = 10
    startTime = [0, 3, 7, 9]
    endTime = [1, 4, 8, 10]
    assert Solution().maxFreeTime(eventTime, startTime, endTime) == 6

    eventTime = 5
    startTime = [0, 1, 2, 3, 4]
    endTime = [1, 2, 3, 4, 5]
    assert Solution().maxFreeTime(eventTime, startTime, endTime) == 0


if __name__ == '__main__':
    main()
