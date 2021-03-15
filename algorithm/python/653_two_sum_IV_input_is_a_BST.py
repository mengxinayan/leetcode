# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.arr = []

        def tree_to_nums(root: TreeNode):
            if root == None:
                pass
            else:
                tree_to_nums(root.left)
                self.arr.append(root.val)
                tree_to_nums(root.right)
        
        tree_to_nums(root)
        left = 0
        right = len(self.arr) - 1
        ans = False
        while left < right:
            if self.arr[left] + self.arr[right] == k:
                ans = True
                break
            elif self.arr[left] + self.arr[right] < k:
                left += 1
            else:
                right -= 1
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
