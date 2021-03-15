# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def node_length(node: TreeNode) -> int:
            if node == None:
                return 0
            left_length = node_length(node.left)
            right_length = node_length(node.right)
            left_len = right_len = 0
            if (node.left != None) and (node.left.val == node.val):
                left_len = left_length + 1
            if (node.right != None) and (node.right.val == node.val):
                right_len = right_length + 1
            self.ans = max(self.ans, left_len+right_len)
            return max(left_len, right_len)

        node_length(root)
        return self.ans

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
