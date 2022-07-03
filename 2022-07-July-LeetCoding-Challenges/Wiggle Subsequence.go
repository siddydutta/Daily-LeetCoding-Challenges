package main

func max(n1, n2 int) int {
	if n1 >= n2 {
		return n1
	}
	return n2
}

func wiggleMaxLength(nums []int) int {
	positive := 1
	negative := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			positive = negative + 1
		} else if nums[i] < nums[i-1] {
			negative = positive + 1
		}
	}
	return max(positive, negative)
}

func main() {
	nums := []int{1, 17, 5, 10, 13, 15, 10, 5, 16, 8}
	expected := 7
	actual := wiggleMaxLength(nums)
	if actual != expected {
		panic("actual differs from expected")
	}
}
