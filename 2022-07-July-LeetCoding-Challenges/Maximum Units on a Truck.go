package main

import "sort"

func min(n1 int, n2 int) int {
	if n1 < n2 {
		return n1
	}
	return n2
}

func maximumUnits(boxTypes [][]int, truckSize int) (boxes int) {
	// sort based on number of units descending
	sort.Slice(boxTypes, func(i, j int) bool {
		return boxTypes[i][1] > boxTypes[j][1]
	})
	for _, boxType := range boxTypes {
		// can only take units <= remaining size
		units := min(boxType[0], truckSize)
		boxes += units * boxType[1]
		truckSize -= units
		if truckSize == 0 {
			return
		}
	}
	return
}

func main() {
	boxTypes := [][]int{
		{1, 3}, {2, 2}, {3, 1},
	}
	truckSize := 4
	expected := 8
	actual := maximumUnits(boxTypes, truckSize)
	if actual != expected {
		panic("actual differs from expected")
	}
}
