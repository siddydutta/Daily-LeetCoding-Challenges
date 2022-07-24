package main

func searchMatrix(matrix [][]int, target int) bool {
    var rows, cols = len(matrix), len(matrix[0])
    // minor optimization to check if target is between min and max
    if target < matrix[0][0] || target > matrix[rows-1][cols-1] {
        return false
    }

    var row, col = 0, cols - 1
    for row < rows && col >= 0 {
        if matrix[row][col] == target {
            return true
        }
        if target < matrix[row][col] {
            // search within same row
            col--
        } else {
            // as not in same row, increment
            row++
        }
    }

    return false
}

func main() {
    matrix := [][]int{{1, 4, 7, 11, 15},
                      {2, 5, 8, 12, 19},
                      {3, 6, 9, 16, 22},
                      {10, 13, 14, 17, 24},
                      {18, 21, 23, 26, 30}}
    target := 5
    expected := true
    actual := searchMatrix(matrix, target)
    if actual != expected {
        panic("actual differs from expected")
    }
}
