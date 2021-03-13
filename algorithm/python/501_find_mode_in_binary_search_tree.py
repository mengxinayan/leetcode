# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        def recursive(root: TreeNode):
            if root != None:
                if root.val not in num_times:
                    num_times[root.val] = 1
                else:
                    num_times[root.val] += 1
                recursive(root.left)
                recursive(root.right)
            else:
                pass

        if root == None: # Don't Forget this case!
            return []
        num_times = {}
        recursive(root)
        max_times = max(num_times.values())
        ans = []
        for key,value in num_times.items():
            if value == max_times:
                ans.append(key)
        return ans

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
