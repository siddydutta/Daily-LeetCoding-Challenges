package main

func max(n1, n2 int) int {
    if n1 >= n2 {
        return n1
    }
    return n2
}

func candy(ratings []int) int {
    n := len(ratings)
    candies := make([]int, n)
    
    // every child must have atleast one candy
    for i := 0; i < n; i++ {
        candies[i] = 1
    }
    
    // left to right to satisfy condition
    for i := 0; i < n-1; i++ {
        if ratings[i+1] > ratings[i] {
            candies[i+1] = max(candies[i]+1, candies[i+1])
        }
    }
    
    // right to left to satisfy condition
    for i := n-2; i >= 0; i-- {
        if ratings[i] > ratings[i+1] {
            candies[i] = max(candies[i+1]+1, candies[i])
        }
    }
    
    sum := 0
    for _, count := range candies {
        sum += count
    }
    return sum
}

func main() {
	ratings := []int{1, 0, 2}
	expected := 5
	actual := candy(ratings)
	if actual != expected {
		panic("actual differs from expected")
	}
}
