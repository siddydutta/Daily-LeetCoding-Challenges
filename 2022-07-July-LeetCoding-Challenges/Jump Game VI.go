package main

func maxResult(nums []int, k int) int {
    deque := []int{0}
    for i := 1; i < len(nums); i++ {
        for len(deque) > 0 && deque[0] < i-k {
            deque = deque[1:]
        }
        nums[i] += nums[deque[0]]
        for len(deque) > 0 && nums[i] >= nums[deque[len(deque)-1]] {
            deque = deque[:len(deque)-1]
        }
        deque = append(deque, i)
    }
    return nums[len(nums)-1]
}

func main() {
    nums := []int{10,-5,-2,4,0,3}
	k := 3
    expected := 17
    actual := maxResult(nums, k)
    if actual != expected {
        panic("actual differs from expected")
    }
}
