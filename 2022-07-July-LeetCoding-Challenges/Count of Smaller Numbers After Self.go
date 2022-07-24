package main

import (
    "reflect"
    "sort"
)


func insert(a []int, index int, value int) []int {
    if len(a) == index {
        return append(a, value)
    }
    a = append(a[:index+1], a[index:]...)
    a[index] = value
    return a
}

func countSmaller(nums []int) []int {
    var sortedList, counts []int

    for i := len(nums)-1; i >= 0; i-- {
        // bisect-left
        index := sort.Search(len(sortedList), func(x int) bool {
            return sortedList[x] >= nums[i]
        })
        // insert count at 0, since traversal is reversed
        counts = insert(counts, 0, index)
        sortedList = insert(sortedList, index, nums[i])
    }

    return counts
}


func main() {
    nums := []int{5, 2, 6, 1}
    expected := []int{2, 1, 1, 0}
    actual := countSmaller(nums)
    if !reflect.DeepEqual(actual, expected) {
    panic("actual differs from expected")
    }
}
