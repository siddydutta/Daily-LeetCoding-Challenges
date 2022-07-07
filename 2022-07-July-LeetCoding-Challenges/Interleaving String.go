package main

func isInterleave(s1 string, s2 string, s3 string) bool {
    // base conditions
    if len(s1) + len(s2) != len(s3) {
        return false
    }
    if len(s3) == 0 {
        return true
    }

    // if last character of s1 and s3 are same
    if len(s1) > 0 && s1[len(s1)-1] == s3[len(s3)-1] {
        if isInterleave(s1[:len(s1)-1], s2, s3[:len(s3)-1]) {
            return true
        }
    }
    // if last character of s2 and s3 are same
    if len(s2) > 0 && s2[len(s2)-1] == s3[len(s3)-1] {
        if isInterleave(s1, s2[:len(s2)-1], s3[:len(s3)-1]) {
            return true
        }
    }

    return false
}

func main() {
    s1 := "aabcc"
    s2 := "dbbca"
    s3 := "aadbbcbcac"
    actual := isInterleave(s1, s2, s3)
    expected := true

    if actual != expected {
        panic("actual differs from expected")
    }
}
