class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = set()
        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i - 2]:
                good.add(num[i-2:i+1])
        return max(good) if good else ''


def main():
    num = "6777133339"
    assert Solution().largestGoodInteger(num) == "777"

    num = "2300019"
    assert Solution().largestGoodInteger(num) == "000"

    num = "42352338"
    assert Solution().largestGoodInteger(num) == ""


if __name__ == '__main__':
    main()
