# -*- coding: utf-8 -*-
class Solution1:
    ''' Stack based solution. '''
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = list()

        for node in preorder:
            # Try to remove processed node and its children
            while stack and node == "#" and stack[-1] == "#":
                stack.pop()
                if not stack:
                    return False
                stack.pop()
            stack.append(node)
        return stack == ["#"]


class Solution:
    '''
    Using concept of indegree and outdegree of nodes.
    Every new node takes away an indegree and adds two outdegrees.
    Time Complexity: O(n)
    '''
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        in_, out = 1, 0  # In degree starts from 1 for the root node
        for node in preorder:
            in_ -= 1  # Take away an indegree
            if abs(in_) > out:
                return False  # As indegree can never greater than outdegree
            if node != '#':
                out += 2  # Add two possible outdegrees, if node is not null
        return abs(in_) == out  # Finally, in and out should match for validity


def main():
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    assert Solution().isValidSerialization(preorder)

    preorder = "1,#"
    assert not Solution().isValidSerialization(preorder)

    preorder = "9,#,#,1"
    assert not Solution().isValidSerialization(preorder)

    preorder = "#,#,3,5,#"
    assert not Solution().isValidSerialization(preorder)


if __name__ == '__main__':
    main()
