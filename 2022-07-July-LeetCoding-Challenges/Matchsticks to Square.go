package main

import "sort"

func makesquare(matchsticks []int) bool {
    // first find sum of all matchstick lengths
    sum := 0
    for _, v := range matchsticks {
        sum += v
    }
    // if total length cannot be divided into four sides, return
    if sum % 4 != 0 {
        return false
    }

    // sort based on descending order of length for minor optimization
    sort.Slice(matchsticks, func(i, j int) bool {
        return matchsticks[i] > matchsticks[j]
    })

    // calculate required length and maintain lengths
    requiredLength, sides := sum / 4, make([]int, 4)
    // backtracking using DFS
    var backtrack func(i int) bool
    backtrack = func(i int) bool {
        if i == len(matchsticks) {
            return true  // last matchstick accounted for
        }
        for j := 0; j < 4; j++ {
            if sides[j] + matchsticks[i] <= requiredLength {
                // if adding side does not exceed required length
                sides[j] += matchsticks[i]
                if backtrack(i + 1) {
                    return true
                }
                // else backtrack
                sides[j] -= matchsticks[i]
            }
        }
        return false
    }

    return backtrack(0)
}

func main() {
    matchsticks := []int{1, 1, 2, 2, 2}
    actual := makesquare(matchsticks)
    expected := true

    if actual != expected {
        panic("actual differs from expected")
    }
}
