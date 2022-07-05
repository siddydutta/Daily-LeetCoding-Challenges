package main

func max(n1, n2 int) int {
    if n1 >= n2 {
        return n1
    }
    return n2
}

func longestConsecutive(nums []int) (maxCount int) {
    numSet := make(map[int]bool)
    // create set of nums
    for _, num := range nums {
        numSet[num] = true
    }

    for num, _ := range numSet {
        count := 1
        // if next lower is present,
        // consecutive is already checked
        if numSet[num-1] {
            continue
        }
        for {
            // check for next consecutive
            if numSet[num+1] {
                num++
                count++
            } else {
                break
            }
        }
        maxCount = max(maxCount, count)
    }
    return maxCount
}

func main() {
    nums := []int{0,3,7,2,5,8,4,6,0,1}
    expected := 9
    actual := longestConsecutive(nums)
    if actual != expected {
        panic("actual differs from expected")
    }
}
