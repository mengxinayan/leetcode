# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root != None and root.left == None and root.right == None:
            return 1
        elif root != None and root.left != None and root.right == None:
            return self.minDepth(root.left)+1
        elif root != None and root.left == None and root.right != None:
            return self.minDepth(root.right)+1
        else:
            return min( self.minDepth(root.left)+1, self.minDepth(root.right)+1 )
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