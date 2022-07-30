package main

import "reflect"

func max(n1, n2 int) int {
    if n1 >= n2 {
        return n1
    }
    return n2
}

func counter(s string) [26]int {
    var freq [26]int
    for _, ch := range s {
        freq[ch - 'a']++
    }
    return freq
}

func wordSubsets(words1 []string, words2 []string) []string {
    var freq2 [26]int
    // compute frequencies of all characters of all words in words2
    for _, word := range words2 {
        freq := counter(word)
        for i := range freq {
            freq2[i] = max(freq2[i], freq[i])
        }
    }

    var result []string
    for _, word := range words1 {
        freq := counter(word)
        flag := true
        // check if word in words1 has >= frequencies than freq2
        for i := range freq2 {
            if freq[i] < freq2[i] {
                flag = false
                break
            }
        }
        if flag {
            result = append(result, word)
        }
    }
    return result
}

func main() {
    words1 := []string{"amazon", "apple", "facebook", "google", "leetcode"}
    words2 := []string{"e", "o"}
    expected := []string{"facebook", "google", "leetcode"}

    actual := wordSubsets(words1, words2)
    if !reflect.DeepEqual(actual, expected) {
        panic("actual differs from expected")
    }
}
