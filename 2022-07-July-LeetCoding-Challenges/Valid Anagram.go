package main

func isAnagram(s string, t string) bool {
    var sCount, tCount [26]int

    for _, ch := range s {
        sCount[ch - 'a']++
    }
    for _, ch := range t {
        tCount[ch - 'a']++
    }

    for i := 0; i < 26; i++ {
        if sCount[i] != tCount[i] {
            return false
        }
    }
    return true
}

func main() {
    s, t := "anagram", "nagaram"
    expected := true
    actual := isAnagram(s, t)
    if actual != expected {
        panic("actual differs from expected")
    }
}
