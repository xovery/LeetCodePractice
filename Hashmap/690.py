"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        result = 0
        queue = collections.deque()
        lookup = {}
        
        for employee in employees:
            lookup[employee.id] = employee

        queue.append(id)

        while queue:
            curr_id = queue.popleft()
            result += lookup[curr_id].importance
            for sub in lookup[curr_id].subordinates:
                queue.append(sub)
        
        return result




        
        