class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1][0] == nums2[ptr2][0]:
                result.append([nums1[ptr1][0], nums1[ptr1][1]+nums2[ptr2][1]])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1][0] > nums2[ptr2][0]:
                result.append(nums2[ptr2])
                ptr2 += 1
            else:
                result.append(nums1[ptr1])
                ptr1 += 1
        result.extend(nums1[ptr1:])
        result.extend(nums2[ptr2:])
        return result


def main():
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    assert Solution().mergeArrays(nums1, nums2) == [[1, 6], [2, 3], [3, 2], [4, 6]]

    nums1 = [[2, 4], [3, 6], [5, 5]]
    nums2 = [[1, 3], [4, 3]]
    assert Solution().mergeArrays(nums1, nums2) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]


if __name__ == '__main__':
    main()
