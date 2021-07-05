# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if (root.left == None) and (root.right == None):
            return -1
        left_val = root.left.val
        right_val = root.right.val
        if left_val == root.val:
            left_val = self.findSecondMinimumValue(root.left)
        if right_val == root.val:
            right_val = self.findSecondMinimumValue(root.right)
        if (left_val != -1) and (right_val != -1):
            return min(left_val, right_val)
        elif (left_val != -1) and (right_val == -1):
            return left_val
        elif (left_val == -1) and (right_val != -1):
            return right_val
        else:
            return -1

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2021  mengxinayan

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
