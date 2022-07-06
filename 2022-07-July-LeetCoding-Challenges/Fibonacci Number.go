package main

// Recursive Solution
func fib1(n int) int {
    if n == 0 || n == 1 {
        return n
    }
    return fib1(n-1) + fib1(n-2)
}

// Iterative Solution
func fib2(n int) int {
    dp := []int{0, 1}
    for i := 2; i <= n; i++ {
        dp = append(dp, dp[i-1] + dp[i-2])
    }
    return dp[n]
}

func main() {
    n := 30
    expected := 832040
    actual1 := fib1(n)
	actual2 := fib2(n)
    if (actual1 != expected) || (actual2 != expected) {
        panic("actual differs from expected")
    }
}
