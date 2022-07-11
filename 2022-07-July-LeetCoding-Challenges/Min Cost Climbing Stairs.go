package main

func min(n1, n2 int) int {
    if n1 <= n2 {
        return n1
    }
    return n2
}

func minCostClimbingStairs(cost []int) int {
    n := len(cost)
    dp := make([]int, n)
    dp[0], dp[1] = cost[0], cost[1]
    for i := 2; i < n; i++ {
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    }
    return min(dp[n-1], dp[n-2])
}

func main() {
    cost := []int{1,100,1,1,1,100,1,1,100,1}
    expected := 6
    actual := minCostClimbingStairs(cost)
    if actual != expected {
        panic("actual differs from expected")
    }
}
