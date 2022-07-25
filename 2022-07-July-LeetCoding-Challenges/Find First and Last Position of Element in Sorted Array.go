package main

import "reflect"

func searchRange(nums []int, target int) []int {
    first, last := 0, len(nums)-1
    start, end := -1, -1

    for first <= last {
        mid := (first + last) / 2
        if nums[mid] == target {
            start = mid
            end = mid
            for start >= 0 && nums[start] == target {
                start -= 1
            }
            start += 1
            for end < len(nums) && nums[end] == target {
                end += 1
            }
            end -= 1
            break
        } else if nums[mid] < target {
            first = mid + 1
        } else {
            last = mid - 1
        }
    }

    return []int{start, end}
}

func main() {
    nums, target := []int{5, 7, 7, 8, 8, 10}, 8
    expected := []int{3, 4}
    actual := searchRange(nums, target)
    if !reflect.DeepEqual(actual, expected) {
        panic("actual differs from expected")
    }
}
