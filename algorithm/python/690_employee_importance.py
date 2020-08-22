# Solution 1

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
        self.res = 0

        def find_subordinates(employees: List['Employee'], id: int) -> Employee:
            res = None
            for employee in employees:
                if employee.id == id:
                    res = employee
            return res
        
        def cal_total_importance(employees: List['Employee'], id: int) -> int:
            employee = find_subordinates(employees, id)
            self.res += employee.importance
            for subordinate_id in employee.subordinates:
                cal_total_importance(employees, subordinate_id)
        
        cal_total_importance(employees, id)
        return self.res


# Solution 2

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
        self.res = 0
        self.employee_dict = {}

        def build_dict(employees: List['Employee']) -> dict:
            for employee in employees:
                self.employee_dict[employee.id] = employee

        def find_employee(id: int) -> Employee:
            return self.employee_dict[id]
        
        def cal_total_importance(id: int) -> int:
            employee = find_employee(id)
            self.res += employee.importance
            for subordinate_id in employee.subordinates:
                cal_total_importance(subordinate_id)
        
        build_dict(employees)
        cal_total_importance(id)
        return self.res

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020  mengxinayan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
