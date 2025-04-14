class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    if abs(arr[i]-arr[j]) <= a and \
                        abs(arr[j]-arr[k]) <= b and \
                            abs(arr[i]-arr[k]) <= c:
                        count += 1
        return count


def main():
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    assert Solution().countGoodTriplets(arr, a, b, c) == 4

    arr = [1, 1, 2, 2, 3]
    a = 0
    b = 0
    c = 1
    assert Solution().countGoodTriplets(arr, a, b, c) == 0


if __name__ == '__main__':
    main()
