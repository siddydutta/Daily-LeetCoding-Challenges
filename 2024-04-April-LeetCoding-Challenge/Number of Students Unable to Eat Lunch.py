from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                i = 0
                while students[i] != sandwiches[0]:
                    i += 1
                    if i == len(students):
                        # no student can eat TOS
                        return i
                students = students[i:] + students[:i]
        return len(students)


def main():
    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]
    assert Solution().countStudents(students, sandwiches) == 0

    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    assert Solution().countStudents(students, sandwiches) == 3


if __name__ == '__main__':
    main()
