class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left, right = 1, max(candies)
        max_candies = 0
        while left <= right:
            mid = left + (right - left) // 2
            n_piles = sum(candy // mid for candy in candies)
            if n_piles >= k:
                max_candies = max(max_candies, mid)
                left = mid + 1
            else:
                right = mid - 1
        return max_candies


def main():
    candies = [5, 8, 6]
    k = 3
    assert Solution().maximumCandies(candies, k) == 5

    candies = [2, 5]
    k = 11
    assert Solution().maximumCandies(candies, k) == 0


if __name__ == '__main__':
    main()
