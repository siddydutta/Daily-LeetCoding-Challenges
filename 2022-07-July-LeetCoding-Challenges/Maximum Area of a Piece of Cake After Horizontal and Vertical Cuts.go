package main

import "sort"

func max(n1, n2 int) int {
    if n1 >= n2 {
        return n1
    }
    return n2
}

func maxDifferenceBetweenConsecutiveElements(array []int) (maxDifference int) {
    sort.Ints(array)
    for i := 1; i < len(array); i++ {
        maxDifference = max(maxDifference, array[i]-array[i-1])
    }
    return
}

func addBorderValues(array []int, edge int) []int {
    array = append([]int{0, edge}, array...)
    return array
}

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
    horizontalCuts = addBorderValues(horizontalCuts, h)
    verticalCuts = addBorderValues(verticalCuts, w)
    
    hDiff := maxDifferenceBetweenConsecutiveElements(horizontalCuts)
    vDiff := maxDifferenceBetweenConsecutiveElements(verticalCuts)
    
    return (hDiff * vDiff) % 1000000007
}

func main() {
	h := 5
	w := 4
	horizontalCuts := []int{1, 2, 4}
	verticalCuts := []int{1, 3}
	expected := 4
	actual := maxArea(h, w, horizontalCuts, verticalCuts)
	if actual != expected {
		panic("actual differs from expected")
	}
}
