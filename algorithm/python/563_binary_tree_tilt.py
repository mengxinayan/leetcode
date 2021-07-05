# Solution 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:

        def node_sum(root: TreeNode) -> int:
            if root == None:
                return 0
            else:
                return root.val + node_sum(root.left) + node_sum(root.right)
        
        if root == None:
            return 0
        else:
            return abs(node_sum(root.left)-node_sum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)


# Solution 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:

        def node_tilt(root: TreeNode) -> int:
            if root == None:
                return 0
            left = node_tilt(root.left)
            right = node_tilt(root.right)
            self.tilt += abs(left-right)
            return root.val + left + right

        self.tilt = 0
        node_tilt(root)
        return self.tilt

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
