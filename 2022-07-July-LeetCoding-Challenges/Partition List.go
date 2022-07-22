package main

// Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
    // dummy nodes marking beginning of lesser and larger ll
    var lessHead, moreHead = &ListNode{}, &ListNode{}
    // actual pointer nodes
    var lessPtr, morePtr = lessHead, moreHead

    for head != nil {
        if head.Val < x {
            // extend lesser ll
            lessPtr.Next = head
            lessPtr = lessPtr.Next
        } else {
            // extend larger ll
            morePtr.Next = head
            morePtr = morePtr.Next
        }
        head = head.Next
    }
    // make lesser ll point to larger ll
    lessPtr.Next = moreHead.Next
    morePtr.Next = nil
    return lessHead.Next
}

func main() {
    head := &ListNode{
            Val: 1,
            Next: &ListNode{
                Val: 4,
                Next: &ListNode{
                    Val: 3,
                    Next: &ListNode{
                        Val: 2,
                        Next: &ListNode{
                            Val: 5,
                            Next: &ListNode{
                                Val: 2,
                            },
                        },
                    },
                },
            },
        }
    x := 3

    expected := &ListNode{
        Val: 1,
        Next: &ListNode{
            Val: 2,
            Next: &ListNode{
                Val: 2,
                Next: &ListNode{
                    Val: 4,
                    Next: &ListNode{
                        Val: 3,
                        Next: &ListNode{
                            Val: 5,
                        },
                    },
                },
            },
        },
    }
    actual := partition(head, x)
    for actual != nil && expected != nil {
        if (actual.Val != expected.Val) {
            panic("actual differs from expected")
        }
        actual = actual.Next
        expected = expected.Next
    }
}
