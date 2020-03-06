# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def cal_node_path(root: TreeNode, now_sum: int) -> int:
            if root == None:
                return 0
            elif (root != None) and (root.left == None) and (root.right == None):
                if now_sum == root.val:
                    return 1
                else:
                    return 0
            else:
                if now_sum == root.val:
                    return 1 + cal_node_path(root.left, now_sum-root.val) \
                             + cal_node_path(root.right, now_sum-root.val)
                else:
                    return cal_node_path(root.left, now_sum-root.val) \ 
                         + cal_node_path(root.right, now_sum-root.val)

        if root == None:
            return 0
        else:
            return cal_node_path(root, sum) + self.pathSum(root.left, sum) \
                 + self.pathSum(root.right, sum)

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
