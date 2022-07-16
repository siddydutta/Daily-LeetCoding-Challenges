package main

const MOD = 1000000007

type Memo struct {
	row   int
	col   int
	moves int
}

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
    cache := make(map[Memo]int)
    var solve func(i, j, maxMove int) int
    solve = func(i, j, maxMove int) int {
        record := Memo{i, j, maxMove}
        if val, ok := cache[record]; ok {
            return val
        }

        if maxMove < 0 {
            return 0
        }
        if i < 0 || i >= m || j < 0 || j >= n {
            return 1
        }
        a := solve(i-1, j, maxMove - 1)
        b := solve(i+1, j, maxMove - 1)
        c := solve(i, j-1, maxMove - 1)
        d := solve(i, j+1, maxMove - 1)

        paths := (a + b + c + d) % MOD
        cache[record] = paths
        return paths
    }
    return solve(startRow, startColumn, maxMove)
}


func main() {
	m, n, maxMove, startRow, startColumn := 8, 7, 16, 1, 5
    expected := 102984580
    actual := findPaths(m, n, maxMove, startRow, startColumn)
    if actual != expected {
        panic("actual differs from expected")
    }
}
