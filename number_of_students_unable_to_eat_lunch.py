from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # sandwiches: Stack
        # students: Queue
        while students != []:
            if len(set(students)) == 1 and students[0] != sandwiches[0]:
                return len(students)
            elif students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                # i = 0?
            else:
                s = students.pop(0)
                students.append(s)

        return len(students)
    
s = Solution()
print(s.countStudents([1,1,0,0], [0,1,0,1]))
print(s.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))